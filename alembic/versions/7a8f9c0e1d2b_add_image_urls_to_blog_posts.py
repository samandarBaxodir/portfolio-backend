"""add image_urls to blog_posts

Revision ID: 7a8f9c0e1d2b
Revises: 40e75e076b50
Create Date: 2026-09-17 18:20:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a8f9c0e1d2b'
down_revision: Union[str, Sequence[str], None] = '40e75e076b50'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('blog_posts', sa.Column('image_urls', sa.JSON(), nullable=True))


def downgrade() -> None:
    op.drop_column('blog_posts', 'image_urls')
