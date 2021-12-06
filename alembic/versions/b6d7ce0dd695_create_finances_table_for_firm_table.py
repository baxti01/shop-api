"""create finances table for firm table

Revision ID: b6d7ce0dd695
Revises: 2f8ba7dc3aa0
Create Date: 2021-12-05 15:50:31.727670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6d7ce0dd695'
down_revision = '2f8ba7dc3aa0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('finances',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('paid_for', sa.Numeric(precision=10, scale=3), nullable=True),
    sa.Column('debt', sa.Numeric(precision=10, scale=3), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('firm_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['firm_id'], ['firms.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('firms', 'paid_for')
    op.drop_column('firms', 'debt')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('firms', sa.Column('debt', sa.NUMERIC(precision=10, scale=3), autoincrement=False, nullable=True))
    op.add_column('firms', sa.Column('paid_for', sa.NUMERIC(precision=10, scale=3), autoincrement=False, nullable=True))
    op.drop_table('finances')
    # ### end Alembic commands ###