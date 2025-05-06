from typing import Any

import firebase_admin
from fastapi import Depends
from firebase_admin import credentials, messaging
from firebase_admin.messaging import BatchResponse

from db.repository.fcm_token import FCMTokenRepository


class NotificationService:
    cred = credentials.Certificate("serviceAccountKey.json")
    default_app = firebase_admin.initialize_app(cred)

    def __init__(self, fcm_token_repo: FCMTokenRepository = Depends()):
        self._fcm_token_repo = fcm_token_repo

    async def add_news(self, title: str, body: str) -> dict[str, Any]:
        tokens = await self._fcm_token_repo.get_tokens()

        if not tokens:
            return {"success_count": 0, "failure_count": 0, "details": [], "message": "No tokens available"}

        message = messaging.MulticastMessage(
            notification=messaging.Notification(title=title, body=body),
            tokens=tokens,
        )

        try:
            batch_response = messaging.send_each_for_multicast(message)

            return self._process_batch_response(batch_response)

        except Exception as e:
            return {
                "success_count": 0,
                "failure_count": len(tokens),
                "details": [{"error": str(e)} for _ in tokens],
                "message": "Failed to send notifications",
            }

    def _process_batch_response(self, batch_response: BatchResponse) -> dict[str, Any]:
        details = []
        for i, response in enumerate(batch_response.responses):
            detail = {
                "token_index": i,
                "success": response.success,
                "message_id": getattr(response, "message_id", None),
            }
            if not response.success:
                detail["error"] = str(response.exception)
            details.append(detail)

        return {
            "success_count": batch_response.success_count,
            "failure_count": batch_response.failure_count,
            "details": details,
            "message": "Notifications processed",
        }
