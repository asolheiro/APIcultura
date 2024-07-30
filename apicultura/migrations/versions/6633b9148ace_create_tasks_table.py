"""create tasks table

Revision ID: 6633b9148ace
Revises: 3049cfa156a6
Create Date: 2024-07-21 13:22:12.813546

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6633b9148ace'
down_revision: Union[str, None] = '3049cfa156a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
