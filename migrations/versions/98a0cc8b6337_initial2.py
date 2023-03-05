"""Initial2

Revision ID: 98a0cc8b6337
Revises: a21e33cbf593
Create Date: 2023-02-20 18:42:50.857625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98a0cc8b6337'
down_revision = 'a21e33cbf593'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('to_dos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Owner', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['Owner'], ['ID_User'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('to_dos', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('Owner')

    # ### end Alembic commands ###
