"""add blockchain table

Revision ID: add_blockchain_table
Revises: 
Create Date: 2024-03-20 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'add_blockchain_table'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('blockchain_data',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('block_index', sa.Integer(), nullable=False),
        sa.Column('block_data', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('blockchain_data') 