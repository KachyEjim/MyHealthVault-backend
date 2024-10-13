"""empty message

Revision ID: 347d0b9ee27f
Revises: 703e91590dea
Create Date: 2024-10-13 16:23:48.561873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '347d0b9ee27f'
down_revision = '703e91590dea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('doctors',
    sa.Column('full_name', sa.String(length=100), nullable=False),
    sa.Column('phone_number', sa.String(length=15), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('specialization', sa.String(length=100), nullable=True),
    sa.Column('license_number', sa.String(length=50), nullable=True),
    sa.Column('hospital_affiliation', sa.String(length=100), nullable=True),
    sa.Column('bio', sa.String(length=500), nullable=True),
    sa.Column('profile_picture', sa.String(length=255), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('license_number')
    )
    op.create_table('appointments',
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('end_time', sa.DateTime(), nullable=False),
    sa.Column('doctor_id', sa.String(length=36), nullable=True),
    sa.Column('user_id', sa.String(length=36), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctors.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('medical_records',
    sa.Column('userId', sa.String(length=50), nullable=False),
    sa.Column('record_name', sa.String(length=200), nullable=False),
    sa.Column('health_care_provider', sa.String(length=100), nullable=False),
    sa.Column('type_of_record', sa.String(length=70), nullable=False),
    sa.Column('diagnosis', sa.String(length=100), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('file_path', sa.String(length=255), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.Column('practitioner_name', sa.String(length=100), nullable=True),
    sa.Column('last_added', sa.DateTime(), nullable=False),
    sa.Column('last_updated', sa.DateTime(), nullable=False),
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('medical_records')
    op.drop_table('appointments')
    op.drop_table('doctors')
    # ### end Alembic commands ###
