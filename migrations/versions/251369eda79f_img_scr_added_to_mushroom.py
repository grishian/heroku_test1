"""img_scr added to mushroom

Revision ID: 251369eda79f
Revises: 563ff01f98af
Create Date: 2022-05-19 21:13:46.853323

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '251369eda79f'
down_revision = '563ff01f98af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mushroom', sa.Column('img_scr', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mushroom', 'img_scr')
    # ### end Alembic commands ###