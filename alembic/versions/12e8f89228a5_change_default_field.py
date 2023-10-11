"""Change Default field

Revision ID: 12e8f89228a5
Revises: 83b1f4c7bbec
Create Date: 2023-10-11 20:25:05.947946

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "12e8f89228a5"
down_revision: Union[str, None] = "83b1f4c7bbec"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
