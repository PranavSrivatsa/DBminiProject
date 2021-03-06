"""empty message

Revision ID: 50f505080f5e
Revises: 
Create Date: 2019-08-23 02:40:40.190164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50f505080f5e'
down_revision = None
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
    sa.UniqueConstraint('email')
    )
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('daycount',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('Carousel', sa.Integer(), nullable=True),
    sa.Column('Darkride', sa.Integer(), nullable=True),
    sa.Column('Droptower', sa.Integer(), nullable=True),
    sa.Column('Ferriswheel', sa.Integer(), nullable=True),
    sa.Column('Gyrotower', sa.Integer(), nullable=True),
    sa.Column('Rollercoaster', sa.Integer(), nullable=True),
    sa.Column('Waterride', sa.Integer(), nullable=True),
    sa.Column('SpiralSlide', sa.Integer(), nullable=True),
    sa.Column('Circus', sa.Integer(), nullable=True),
    sa.Column('Gravitron', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('daydetails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('day_rev', sa.Integer(), nullable=True),
    sa.Column('day_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dayrev',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('Carousel', sa.Integer(), nullable=True),
    sa.Column('Darkride', sa.Integer(), nullable=True),
    sa.Column('Droptower', sa.Integer(), nullable=True),
    sa.Column('Ferriswheel', sa.Integer(), nullable=True),
    sa.Column('Gyrotower', sa.Integer(), nullable=True),
    sa.Column('Rollercoaster', sa.Integer(), nullable=True),
    sa.Column('Waterride', sa.Integer(), nullable=True),
    sa.Column('SpiralSlide', sa.Integer(), nullable=True),
    sa.Column('Circus', sa.Integer(), nullable=True),
    sa.Column('Gravitron', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('monthcount',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('Carousel', sa.Integer(), nullable=True),
    sa.Column('Darkride', sa.Integer(), nullable=True),
    sa.Column('Droptower', sa.Integer(), nullable=True),
    sa.Column('Ferriswheel', sa.Integer(), nullable=True),
    sa.Column('Gyrotower', sa.Integer(), nullable=True),
    sa.Column('Rollercoaster', sa.Integer(), nullable=True),
    sa.Column('Waterride', sa.Integer(), nullable=True),
    sa.Column('SpiralSlide', sa.Integer(), nullable=True),
    sa.Column('Circus', sa.Integer(), nullable=True),
    sa.Column('Gravitron', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('monthdetails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('month_rev', sa.Integer(), nullable=True),
    sa.Column('month_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('monthrev',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('Carousel', sa.Integer(), nullable=True),
    sa.Column('Darkride', sa.Integer(), nullable=True),
    sa.Column('Droptower', sa.Integer(), nullable=True),
    sa.Column('Ferriswheel', sa.Integer(), nullable=True),
    sa.Column('Gyrotower', sa.Integer(), nullable=True),
    sa.Column('Rollercoaster', sa.Integer(), nullable=True),
    sa.Column('Waterride', sa.Integer(), nullable=True),
    sa.Column('SpiralSlide', sa.Integer(), nullable=True),
    sa.Column('Circus', sa.Integer(), nullable=True),
    sa.Column('Gravitron', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ride',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('maintenance_cost', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('customerrides',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customerId', sa.Integer(), nullable=True),
    sa.Column('rideId', sa.Integer(), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['customerId'], ['customer.id'], ),
    sa.ForeignKeyConstraint(['rideId'], ['ride.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customerrides')
    op.drop_table('ride')
    op.drop_table('monthrev')
    op.drop_table('monthdetails')
    op.drop_table('monthcount')
    op.drop_table('dayrev')
    op.drop_table('daydetails')
    op.drop_table('daycount')
    op.drop_table('customer')
    op.drop_table('account')
    # ### end Alembic commands ###
