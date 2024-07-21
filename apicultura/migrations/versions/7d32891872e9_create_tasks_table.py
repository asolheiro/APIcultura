"""create tasks table

Revision ID: 7d32891872e9
Revises: cd6ff3711935
Create Date: 2024-07-21 14:12:19.835494

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d32891872e9'
down_revision: Union[str, None] = 'cd6ff3711935'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
