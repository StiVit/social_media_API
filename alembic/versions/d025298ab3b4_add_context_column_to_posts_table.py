"""Add context column to posts table

Revision ID: d025298ab3b4
Revises: 77bec6822883
Create Date: 2025-02-09 15:31:24.778241

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd025298ab3b4'
down_revision: Union[str, None] = '77bec6822883'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'context')
    pass
