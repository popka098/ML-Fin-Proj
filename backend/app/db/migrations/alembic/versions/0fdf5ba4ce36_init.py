"""init

Revision ID: 0fdf5ba4ce36
Revises: f6ae32b83d83
Create Date: 2026-04-29 21:44:40.781360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0fdf5ba4ce36'
down_revision: Union[str, Sequence[str], None] = 'f6ae32b83d83'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
