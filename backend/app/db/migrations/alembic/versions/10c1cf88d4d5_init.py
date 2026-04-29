"""init

Revision ID: 10c1cf88d4d5
Revises: 0fdf5ba4ce36
Create Date: 2026-04-29 21:50:39.877063

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '10c1cf88d4d5'
down_revision: Union[str, Sequence[str], None] = '0fdf5ba4ce36'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
