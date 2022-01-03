"""add content column to posts table

Revision ID: 437b7283ca3c
Revises: e786c607d5ef
Create Date: 2022-01-02 22:20:24.026023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '437b7283ca3c'
down_revision = 'e786c607d5ef'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(512), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
