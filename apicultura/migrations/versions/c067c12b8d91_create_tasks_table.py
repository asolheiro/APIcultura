"""create tasks table

Revision ID: c067c12b8d91
Revises: 6633b9148ace
Create Date: 2024-07-21 13:37:53.363922

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c067c12b8d91'
down_revision: Union[str, None] = '6633b9148ace'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
