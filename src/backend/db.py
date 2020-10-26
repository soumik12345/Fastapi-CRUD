import os
import sqlalchemy
from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata = sqlalchemy.MetaData()
notes = sqlalchemy.Table(
    "notes", metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(50)),
    sqlalchemy.Column("description", sqlalchemy.String(50)),
    sqlalchemy.Column(
        "created_date", sqlalchemy.DateTime,
        default=sqlalchemy.sql.func.now(), nullable=False
    ),
)

# databases query builder
database = Database(DATABASE_URL)
