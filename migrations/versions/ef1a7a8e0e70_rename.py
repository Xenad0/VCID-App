"""Rename

Revision ID: ef1a7a8e0e70
Revises: cd7426ada008
Create Date: 2023-03-08 21:23:27.860091

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ef1a7a8e0e70'
down_revision = 'cd7426ada008'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('updates',
    sa.Column('ID_Update', sa.Integer(), nullable=False),
    sa.Column('Titel', sa.String(length=64), nullable=True),
    sa.Column('Content', sa.String(length=256), nullable=True),
    sa.Column('Timestamp', sa.DateTime(), nullable=True),
    sa.Column('User_ID', sa.Integer(), nullable=True),
    sa.Column('ToDo_ID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ToDo_ID'], ['to_dos.ID_ToDo'], ),
    sa.ForeignKeyConstraint(['User_ID'], ['users.ID_User'], ),
    sa.PrimaryKeyConstraint('ID_Update')
    )
    op.drop_table('comments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('ID_Comment', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('Titel', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('Content', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('Timestamp', mysql.DATETIME(), nullable=True),
    sa.Column('User_ID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ToDo_ID', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['ToDo_ID'], ['to_dos.ID_ToDo'], name='comments_ibfk_1'),
    sa.ForeignKeyConstraint(['User_ID'], ['users.ID_User'], name='comments_ibfk_2'),
    sa.PrimaryKeyConstraint('ID_Comment'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.drop_table('updates')
    # ### end Alembic commands ###
