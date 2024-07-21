"""create tasks table

Revision ID: 2a28aad461a5
Revises: 7d32891872e9
Create Date: 2024-07-21 14:16:15.551278

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2a28aad461a5'
down_revision: Union[str, None] = '7d32891872e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
