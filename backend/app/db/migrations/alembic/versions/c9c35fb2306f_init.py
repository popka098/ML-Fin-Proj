"""init

Revision ID: c9c35fb2306f
Revises: a42f2c626f25
Create Date: 2026-04-29 21:55:46.981664

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9c35fb2306f'
down_revision: Union[str, Sequence[str], None] = 'a42f2c626f25'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
