"""init

Revision ID: a13f3be60697
Revises: c9c35fb2306f
Create Date: 2026-04-29 22:16:54.101764

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a13f3be60697'
down_revision: Union[str, Sequence[str], None] = 'c9c35fb2306f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
