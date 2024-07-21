"""create tasks table

Revision ID: 1f599da59d38
Revises: a241378c0fd3
Create Date: 2024-07-21 17:06:49.197603

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1f599da59d38'
down_revision: Union[str, None] = 'a241378c0fd3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
