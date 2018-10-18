"""empty message

Revision ID: f5450eec254e
Revises: 888b38ae3411
Create Date: 2018-10-18 20:49:25.404609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5450eec254e'
down_revision = '888b38ae3411'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('fullname')
    )
    op.drop_table('accounts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('fullname', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='accounts_pkey'),
    sa.UniqueConstraint('email', name='accounts_email_key'),
    sa.UniqueConstraint('fullname', name='accounts_fullname_key')
    )
    op.drop_table('account')
    # ### end Alembic commands ###