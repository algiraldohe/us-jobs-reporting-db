"""Add operationalisation fields

Revision ID: e0355c8e4af3
Revises: d89f010675e0
Create Date: 2023-08-30 09:34:01.603168

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0355c8e4af3'
down_revision: Union[str, None] = 'd89f010675e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jobs', sa.Column('StorageFile', sa.String(), nullable=True))
    op.add_column('jobs', sa.Column('DateAdded', sa.DateTime(), nullable=True))
    op.add_column('jobs', sa.Column('UserAdded', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('jobs', 'UserAdded')
    op.drop_column('jobs', 'DateAdded')
    op.drop_column('jobs', 'StorageFile')
    # ### end Alembic commands ###