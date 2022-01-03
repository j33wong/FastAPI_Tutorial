"""add foreign-key to posts table

Revision ID: 407f9ee27810
Revises: df21021adbe0
Create Date: 2022-01-02 22:31:24.393468

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import table


# revision identifiers, used by Alembic.
revision = '407f9ee27810'
down_revision = 'df21021adbe0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('posts_users_FK', source_table="posts", referent_table="users", local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('posts_users_FK', table_name="posts", type_='foreignkey')
    op.drop_column('posts', 'owner_id')
    pass
