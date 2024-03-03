"""add business banenr

Revision ID: d05961818362
Revises: 21849848b74f
Create Date: 2024-03-03 15:04:42.446479

"""
from typing import Sequence
from typing import Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'd05961818362'
down_revision: Union[str, None] = '21849848b74f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('businesses', sa.Column('description', sa.String(length=1000), nullable=True))
    op.add_column('businesses', sa.Column('banner_id', sa.Integer(), nullable=True))
    op.create_foreign_key('business_banner_fkey', 'businesses', 'attachments', ['banner_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('business_banner_fkey', 'businesses', type_='foreignkey')
    op.drop_column('businesses', 'banner_id')
    op.drop_column('businesses', 'description')
    # ### end Alembic commands ###
