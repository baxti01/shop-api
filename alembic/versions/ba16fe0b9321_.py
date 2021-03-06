"""empty message

Revision ID: ba16fe0b9321
Revises: 
Create Date: 2022-02-13 20:44:39.287294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba16fe0b9321'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('chief', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('cash_box',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cash', sa.Numeric(precision=10, scale=3), nullable=True),
    sa.Column('card', sa.Numeric(precision=10, scale=3), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cash_box_user_id'), 'cash_box', ['user_id'], unique=False)
    op.create_table('debtors',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('paid', sa.Numeric(precision=10, scale=3), nullable=True),
    sa.Column('debt', sa.Numeric(precision=10, scale=3), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_debtors_user_id'), 'debtors', ['user_id'], unique=False)
    op.create_table('firms',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_firms_user_id'), 'firms', ['user_id'], unique=False)
    op.create_table('shopping_list',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('purchased', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_shopping_list_user_id'), 'shopping_list', ['user_id'], unique=False)
    op.create_table('expenses',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=3), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('firm_flag', sa.Boolean(), nullable=True),
    sa.Column('firm_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['firm_id'], ['firms.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_expenses_firm_id'), 'expenses', ['firm_id'], unique=False)
    op.create_index(op.f('ix_expenses_user_id'), 'expenses', ['user_id'], unique=False)
    op.create_table('finances',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('paid', sa.Numeric(precision=10, scale=3), nullable=True),
    sa.Column('debt', sa.Numeric(precision=10, scale=3), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('firm_id', sa.Integer(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['firm_id'], ['firms.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('invoices',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('image_id', sa.String(), nullable=True),
    sa.Column('image_uri', sa.String(), nullable=True),
    sa.Column('to_pay', sa.Numeric(precision=10, scale=3), nullable=True),
    sa.Column('paid', sa.Numeric(precision=10, scale=3), nullable=True),
    sa.Column('previous_debt', sa.Numeric(precision=10, scale=3), nullable=True),
    sa.Column('debt', sa.Numeric(precision=10, scale=3), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('firm_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['firm_id'], ['firms.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('image_id')
    )
    op.create_index(op.f('ix_invoices_firm_id'), 'invoices', ['firm_id'], unique=False)
    op.create_index(op.f('ix_invoices_user_id'), 'invoices', ['user_id'], unique=False)
    op.create_table('products',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('count', sa.Float(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=3), nullable=True),
    sa.Column('total_price', sa.Numeric(precision=10, scale=3), nullable=True),
    sa.Column('invoice_id', sa.Integer(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['invoice_id'], ['invoices.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_products_company_id'), 'products', ['company_id'], unique=False)
    op.create_index(op.f('ix_products_invoice_id'), 'products', ['invoice_id'], unique=False)
    op.create_index(op.f('ix_products_user_id'), 'products', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_products_user_id'), table_name='products')
    op.drop_index(op.f('ix_products_invoice_id'), table_name='products')
    op.drop_index(op.f('ix_products_company_id'), table_name='products')
    op.drop_table('products')
    op.drop_index(op.f('ix_invoices_user_id'), table_name='invoices')
    op.drop_index(op.f('ix_invoices_firm_id'), table_name='invoices')
    op.drop_table('invoices')
    op.drop_table('finances')
    op.drop_index(op.f('ix_expenses_user_id'), table_name='expenses')
    op.drop_index(op.f('ix_expenses_firm_id'), table_name='expenses')
    op.drop_table('expenses')
    op.drop_index(op.f('ix_shopping_list_user_id'), table_name='shopping_list')
    op.drop_table('shopping_list')
    op.drop_index(op.f('ix_firms_user_id'), table_name='firms')
    op.drop_table('firms')
    op.drop_index(op.f('ix_debtors_user_id'), table_name='debtors')
    op.drop_table('debtors')
    op.drop_index(op.f('ix_cash_box_user_id'), table_name='cash_box')
    op.drop_table('cash_box')
    op.drop_table('users')
    op.drop_table('company')
    # ### end Alembic commands ###
