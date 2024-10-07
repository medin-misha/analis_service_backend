"""upgrade analisstandart

Revision ID: 1ba20ac9999f
Revises: 23836f5ff813
Create Date: 2024-10-06 16:27:01.392131

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ba20ac9999f'
down_revision: Union[str, None] = '23836f5ff813'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('analisstandarts', sa.Column('age_min', sa.Integer(), nullable=False))
    op.add_column('analisstandarts', sa.Column('age_max', sa.Integer(), nullable=False))
    op.add_column('analisstandarts', sa.Column('weight_min', sa.Integer(), nullable=False))
    op.add_column('analisstandarts', sa.Column('weight_max', sa.Integer(), nullable=False))
    op.drop_column('analisstandarts', 'age')
    op.drop_column('analisstandarts', 'weight')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('analisstandarts', sa.Column('weight', sa.INTEGER(), nullable=False))
    op.add_column('analisstandarts', sa.Column('age', sa.INTEGER(), nullable=False))
    op.drop_column('analisstandarts', 'weight_max')
    op.drop_column('analisstandarts', 'weight_min')
    op.drop_column('analisstandarts', 'age_max')
    op.drop_column('analisstandarts', 'age_min')
    # ### end Alembic commands ###