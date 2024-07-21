"""create tasks table

Revision ID: a241378c0fd3
Revises: 75bf6c5d142c
Create Date: 2024-07-21 17:06:46.851930

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a241378c0fd3'
down_revision: Union[str, None] = '75bf6c5d142c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
