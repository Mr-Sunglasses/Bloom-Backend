"""Changed the default values of some fields

Revision ID: 0902da57a42d
Revises: 6bf2d73c7f2c
Create Date: 2023-10-11 20:16:10.474737

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0902da57a42d"
down_revision: Union[str, None] = "6bf2d73c7f2c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###