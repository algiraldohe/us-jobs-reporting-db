"""Create location field

Revision ID: 4a99a899b215
Revises: f9a8a411c3d3
Create Date: 2023-08-29 13:42:31.379146

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a99a899b215'
down_revision: Union[str, None] = 'f9a8a411c3d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jobs', sa.Column('location', sa.JSON(), nullable=True))
    op.drop_column('jobs', 'description')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jobs', sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('jobs', 'location')
    # ### end Alembic commands ###
