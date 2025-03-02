"""add deleted at to offer

Revision ID: 7975dd572d0f
Revises: d05961818362
Create Date: 2024-03-03 15:49:47.392127

"""
from typing import Sequence
from typing import Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '7975dd572d0f'
down_revision: Union[str, None] = 'd05961818362'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('offers', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('offers', 'deleted_at')
    # ### end Alembic commands ###
