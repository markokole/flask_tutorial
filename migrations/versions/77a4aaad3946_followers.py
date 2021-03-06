"""followers

Revision ID: 77a4aaad3946
Revises: 02855ec5e22e
Create Date: 2018-07-07 21:02:53.529475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77a4aaad3946'
down_revision = '02855ec5e22e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
