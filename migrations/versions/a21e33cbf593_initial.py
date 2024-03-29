"""Initial

Revision ID: a21e33cbf593
Revises: 
Create Date: 2023-02-20 10:08:05.318416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a21e33cbf593'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('ID_User', sa.Integer(), nullable=False),
    sa.Column('Username', sa.String(length=64), nullable=True),
    sa.Column('Givenname', sa.String(length=64), nullable=True),
    sa.Column('Surname', sa.String(length=64), nullable=True),
    sa.Column('Mail', sa.String(length=128), nullable=True),
    sa.Column('Password', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('ID_User')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_users_Mail'), ['Mail'], unique=True)
        batch_op.create_index(batch_op.f('ix_users_Username'), ['Username'], unique=True)

    op.create_table('to_dos',
    sa.Column('ID_ToDo', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=64), nullable=True),
    sa.Column('Description', sa.String(length=128), nullable=True),
    sa.Column('Status', sa.String(length=16), nullable=True),
    sa.Column('Date', sa.DateTime(), nullable=True),
    sa.Column('User_ID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['User_ID'], ['users.ID_User'], ),
    sa.PrimaryKeyConstraint('ID_ToDo')
    )
    op.create_table('comments',
    sa.Column('ID_Comment', sa.Integer(), nullable=False),
    sa.Column('Titel', sa.String(length=64), nullable=True),
    sa.Column('Content', sa.String(length=256), nullable=True),
    sa.Column('Timestamp', sa.DateTime(), nullable=True),
    sa.Column('User_ID', sa.Integer(), nullable=True),
    sa.Column('ToDo_ID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ToDo_ID'], ['to_dos.ID_ToDo'], ),
    sa.ForeignKeyConstraint(['User_ID'], ['users.ID_User'], ),
    sa.PrimaryKeyConstraint('ID_Comment')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.drop_table('to_dos')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_Username'))
        batch_op.drop_index(batch_op.f('ix_users_Mail'))

    op.drop_table('users')
    # ### end Alembic commands ###
