"""added temperature table

Revision ID: ec1b3a792535
Revises: 8ef4a9a2c3a8
Create Date: 2022-05-19 16:26:25.415458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec1b3a792535'
down_revision = '8ef4a9a2c3a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('temperature',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('celsius', sa.Integer(), nullable=True),
    sa.Column('grow_run_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['grow_run_id'], ['grow_run.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_temperature_grow_run_id'), 'temperature', ['grow_run_id'], unique=False)
    op.create_index(op.f('ix_temperature_id'), 'temperature', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_temperature_id'), table_name='temperature')
    op.drop_index(op.f('ix_temperature_grow_run_id'), table_name='temperature')
    op.drop_table('temperature')
    # ### end Alembic commands ###
