"""testing Changes

Revision ID: 3d7cc643c9dd
Revises: d07fb699344b
Create Date: 2023-10-11 20:36:26.260094

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3d7cc643c9dd"
down_revision: Union[str, None] = "d07fb699344b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
