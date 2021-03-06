from .models import NoteSchema
from ..db import notes, database


async def post(payload: NoteSchema):
    query = notes.insert().values(
        title=payload.title, description=payload.description
    )
    return await database.execute(query)
