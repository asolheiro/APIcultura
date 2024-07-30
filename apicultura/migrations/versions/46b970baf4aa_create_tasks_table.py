"""create tasks table

Revision ID: 46b970baf4aa
Revises: c067c12b8d91
Create Date: 2024-07-21 13:48:28.458083

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46b970baf4aa'
down_revision: Union[str, None] = 'c067c12b8d91'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
