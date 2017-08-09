"""add collect posts

Revision ID: 120804c3552d
Revises: b9a8a1b63b4f
Create Date: 2017-08-08 16:07:41.367834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '120804c3552d'
down_revision = 'b9a8a1b63b4f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('collection',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('collection')
    # ### end Alembic commands ###
