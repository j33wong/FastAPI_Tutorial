"""create posts table

Revision ID: e786c607d5ef
Revises: 
Create Date: 2022-01-02 22:09:51.593632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e786c607d5ef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(256), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
