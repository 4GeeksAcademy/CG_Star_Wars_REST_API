"""empty message

Revision ID: 0a9afa495c70
Revises: a369a1a6f564
Create Date: 2023-06-03 18:17:41.970613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a9afa495c70'
down_revision = 'a369a1a6f564'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=True),
    sa.Column('rotation_period', sa.Integer(), nullable=True),
    sa.Column('orbital_period', sa.Integer(), nullable=True),
    sa.Column('gravity', sa.String(), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('climate', sa.String(), nullable=True),
    sa.Column('terrain', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('planets')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('diameter', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('rotation_period', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('orbital_period', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('gravity', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('population', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('climate', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('terrain', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='planets_pkey')
    )
    op.drop_table('planet')
    # ### end Alembic commands ###
