"""empty message

Revision ID: 1760a6b07ae3
Revises: 
Create Date: 2019-12-25 19:35:57.392127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1760a6b07ae3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('calls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('caller_number', sa.String(length=50), nullable=False),
    sa.Column('target_number', sa.String(length=50), nullable=False),
    sa.Column('call_started_time', sa.DateTime(), nullable=False),
    sa.Column('call_ended_time', sa.DateTime(), nullable=False),
    sa.Column('cost', sa.Numeric(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tariffs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('connection_type', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Numeric(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tariffs')
    op.drop_table('calls')
    # ### end Alembic commands ###
