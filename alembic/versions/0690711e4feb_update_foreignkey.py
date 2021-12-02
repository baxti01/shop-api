"""update foreignkey

Revision ID: 0690711e4feb
Revises: d5994d8dc0c1
Create Date: 2021-11-30 16:43:33.014086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0690711e4feb'
down_revision = 'd5994d8dc0c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('invoices_user_id_fkey', 'invoices', type_='foreignkey')
    op.create_foreign_key(None, 'invoices', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'invoices', type_='foreignkey')
    op.create_foreign_key('invoices_user_id_fkey', 'invoices', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###