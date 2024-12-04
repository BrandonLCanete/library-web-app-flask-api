"""add progress table

Revision ID: b1a7e0b7fccc
Revises: e2aecc2b6480
Create Date: 2024-12-04 22:48:29.150512

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b1a7e0b7fccc'
down_revision = 'e2aecc2b6480'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('progress',
    sa.Column('progress_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('progress_uuid', mysql.CHAR(length=36), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('chapter_id', sa.Integer(), nullable=False),
    sa.Column('progress_percentage', sa.DECIMAL(), nullable=False),
    sa.Column('last_read_at', sa.DateTime(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.book_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('progress_id'),
    sa.UniqueConstraint('progress_uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('progress')
    # ### end Alembic commands ###
