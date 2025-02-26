"""del username

Revision ID: af4561630ac1
Revises: fec16d67231b
Create Date: 2025-02-26 17:02:53.282861

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "af4561630ac1"
down_revision: Union[str, None] = "fec16d67231b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "uq_weather_records_username", "weather_records", type_="unique"
    )
    op.drop_column("weather_records", "username")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "weather_records",
        sa.Column(
            "username", sa.VARCHAR(), autoincrement=False, nullable=False
        ),
    )
    op.create_unique_constraint(
        "uq_weather_records_username", "weather_records", ["username"]
    )
    # ### end Alembic commands ###
