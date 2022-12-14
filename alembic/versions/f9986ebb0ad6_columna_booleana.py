"""columna booleana

Revision ID: f9986ebb0ad6
Revises: 
Create Date: 2022-09-05 16:13:09.900401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9986ebb0ad6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('productos', sa.Column('estaActivado', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('productos', 'estaActivado')
    # ### end Alembic commands ###
