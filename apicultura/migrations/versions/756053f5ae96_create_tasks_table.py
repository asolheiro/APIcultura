"""create tasks table

Revision ID: 756053f5ae96
Revises: 46b970baf4aa
Create Date: 2024-07-21 13:56:08.294264

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '756053f5ae96'
down_revision: Union[str, None] = '46b970baf4aa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
