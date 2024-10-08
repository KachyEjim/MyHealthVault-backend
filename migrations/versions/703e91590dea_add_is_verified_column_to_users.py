"""Add is_verified column to users

Revision ID: 703e91590dea
Revises: 
Create Date: 2024-10-06 07:29:20.248587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '703e91590dea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_verified', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('is_verified')

    # ### end Alembic commands ###
