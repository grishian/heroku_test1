"""added grow_run table

Revision ID: 8ef4a9a2c3a8
Revises: 860ef4decd54
Create Date: 2022-05-19 16:18:26.337827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ef4a9a2c3a8'
down_revision = '860ef4decd54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grow_run',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mushroom_id', sa.Integer(), nullable=True),
    sa.Column('mushroom_stage', sa.Integer(), nullable=True),
    sa.Column('grow_start', sa.DateTime(), nullable=True),
    sa.Column('spawn_start', sa.DateTime(), nullable=True),
    sa.Column('fruit_start', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['mushroom_id'], ['mushroom.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_grow_run_id'), 'grow_run', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_grow_run_id'), table_name='grow_run')
    op.drop_table('grow_run')
    # ### end Alembic commands ###
