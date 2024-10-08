"""new_migration_name

Revision ID: 5fed2152714e
Revises: 
Create Date: 2024-08-09 11:36:36.175626

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5fed2152714e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo_list',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('todo_item',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('list_id', sa.UUID(), nullable=False),
    sa.Column('completed', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['list_id'], ['todo_list.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo_item')
    op.drop_table('todo_list')
    # ### end Alembic commands ###
