"""Added tables for news

Revision ID: 384a2d961434
Revises:
Create Date: 2025-02-16 15:06:57.379139

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "384a2d961434"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "news_category",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("news_category_pkey")),
        sa.UniqueConstraint("name", name=op.f("news_category_name_key")),
    )
    op.create_index(op.f("news_category_id_idx"), "news_category", ["id"], unique=False)
    op.create_table(
        "users",
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("users_pkey")),
        sa.UniqueConstraint("email", name=op.f("users_email_key")),
        sa.UniqueConstraint("username", name=op.f("users_username_key")),
    )
    op.create_index(op.f("users_id_idx"), "users", ["id"], unique=False)
    op.create_table(
        "news",
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("content", sa.String(), nullable=False),
        sa.Column("author_id", sa.Integer(), nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["author_id"], ["users.id"], name=op.f("news_author_id_fkey")),
        sa.ForeignKeyConstraint(["category_id"], ["news_category.id"], name=op.f("news_category_id_fkey")),
        sa.PrimaryKeyConstraint("id", name=op.f("news_pkey")),
        sa.UniqueConstraint("title", name=op.f("news_title_key")),
    )
    op.create_index(op.f("news_id_idx"), "news", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("news_id_idx"), table_name="news")
    op.drop_table("news")
    op.drop_index(op.f("users_id_idx"), table_name="users")
    op.drop_table("users")
    op.drop_index(op.f("news_category_id_idx"), table_name="news_category")
    op.drop_table("news_category")
    # ### end Alembic commands ###
