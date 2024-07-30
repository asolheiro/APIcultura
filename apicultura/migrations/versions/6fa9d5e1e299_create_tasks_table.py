"""create tasks table

Revision ID: 6fa9d5e1e299
Revises: 756053f5ae96
Create Date: 2024-07-21 14:01:45.067300

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6fa9d5e1e299'
down_revision: Union[str, None] = '756053f5ae96'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
