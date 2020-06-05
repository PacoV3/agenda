"""Initial migration

Revision ID: e60f18d28185
Revises: a2af276ff41c
Create Date: 2020-06-02 22:43:20.014664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e60f18d28185'
down_revision = 'a2af276ff41c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=True),
    sa.Column('telefono', sa.String(length=12), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contacts_email'), 'contacts', ['email'], unique=True)
    op.create_index(op.f('ix_contacts_nombre'), 'contacts', ['nombre'], unique=False)
    op.create_index(op.f('ix_contacts_telefono'), 'contacts', ['telefono'], unique=True)
    op.create_index(op.f('ix_contacts_timestamp'), 'contacts', ['timestamp'], unique=False)
    op.drop_index('ix_posts_timestamp', table_name='posts')
    op.drop_table('posts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('body', sa.VARCHAR(length=280), nullable=True),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.Column('users_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_posts_timestamp', 'posts', ['timestamp'], unique=False)
    op.drop_index(op.f('ix_contacts_timestamp'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_telefono'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_nombre'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_email'), table_name='contacts')
    op.drop_table('contacts')
    # ### end Alembic commands ###
