"""empty message

Revision ID: c58d82f2c2df
Revises: 
Create Date: 2019-07-25 16:39:54.650704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c58d82f2c2df'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('sno', sa.String(length=11), nullable=True),
    sa.Column('sname', sa.String(length=30), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('sno')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    # ### end Alembic commands ###