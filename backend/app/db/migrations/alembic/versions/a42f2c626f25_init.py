"""init

Revision ID: a42f2c626f25
Revises: 10c1cf88d4d5
Create Date: 2026-04-29 21:54:43.157762

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a42f2c626f25'
down_revision: Union[str, Sequence[str], None] = '10c1cf88d4d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
