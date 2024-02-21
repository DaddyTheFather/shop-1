"""Create features table

Revision ID: f7438d9d1642
Revises: 6a68e3a5c60a
Create Date: 2024-02-21 15:38:24.513149

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "f7438d9d1642"
down_revision: Union[str, None] = "6a68e3a5c60a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "features",
        sa.Column("feature_id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.BIGINT(), nullable=False),
        sa.Column("username", sa.String()),
        sa.Column("feature_message", sa.String(1000)),
        sa.Column("status", sa.String(), server_default="New"),
        sa.Column("software", sa.String()),
        sa.Column("created_at", sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.user_id"]),
        sa.PrimaryKeyConstraint("feature_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("features")
    # ### end Alembic commands ###
