"""Add phone_number to users table

Revision ID: 6279be949c6f
Revises: 5b5c39d45b79
Create Date: 2025-08-11 17:20:43.611464

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6279be949c6f'
down_revision: Union[str, Sequence[str], None] = '5b5c39d45b79'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
