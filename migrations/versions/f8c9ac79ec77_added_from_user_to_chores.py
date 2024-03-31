"""added from user to chores

Revision ID: f8c9ac79ec77
Revises: 7f5c9aed03d5
Create Date: 2024-03-31 01:34:42.724914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8c9ac79ec77'
down_revision = '7f5c9aed03d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chores', schema=None) as batch_op:
        batch_op.add_column(sa.Column('from_user_id', sa.Integer(), nullable=True))
        batch_op.alter_column('repeat_time',
               existing_type=sa.DATE(),
               type_=sa.Integer(),
               existing_nullable=True)
        batch_op.create_foreign_key('fk_chores_from_users_id', 'users', ['from_user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chores', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('repeat_time',
               existing_type=sa.Integer(),
               type_=sa.DATE(),
               existing_nullable=True)
        batch_op.drop_column('from_user_id')

    # ### end Alembic commands ###
