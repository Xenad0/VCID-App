"""empty message

Revision ID: cd7426ada008
Revises: 8d5cd1e26793
Create Date: 2023-03-07 23:53:48.930265

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cd7426ada008'
down_revision = '8d5cd1e26793'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('to_dos', schema=None) as batch_op:
        batch_op.alter_column('Description',
               existing_type=mysql.VARCHAR(length=128),
               type_=sa.String(length=1024),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('to_dos', schema=None) as batch_op:
        batch_op.alter_column('Description',
               existing_type=sa.String(length=1024),
               type_=mysql.VARCHAR(length=128),
               existing_nullable=True)

    # ### end Alembic commands ###
