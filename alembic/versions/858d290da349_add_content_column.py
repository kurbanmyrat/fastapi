"""add content column

Revision ID: 858d290da349
Revises: eaee14c592e7
Create Date: 2023-08-17 06:25:04.805728

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '858d290da349'
down_revision: Union[str, None] = 'eaee14c592e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    pass
