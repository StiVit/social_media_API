"""Add foreign key to posts table

Revision ID: 858dbd0d5c00
Revises: 64d57278c34d
Create Date: 2025-02-09 15:42:12.226944

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '858dbd0d5c00'
down_revision: Union[str, None] = '64d57278c34d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable = False))
    op.create_foreign_key('posts_users_fk', 'posts', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', 'posts', type_='foreignkey')
    op.drop_column('posts', 'user_id')
    pass
