"""init

Revision ID: f6ae32b83d83
Revises: 39737760250f
Create Date: 2026-04-29 21:38:15.591074

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6ae32b83d83'
down_revision: Union[str, Sequence[str], None] = '39737760250f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
