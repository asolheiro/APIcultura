"""create tasks table

Revision ID: 75bf6c5d142c
Revises: 2a28aad461a5
Create Date: 2024-07-21 14:17:21.506339

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75bf6c5d142c'
down_revision: Union[str, None] = '2a28aad461a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
