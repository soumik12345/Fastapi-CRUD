from fastapi import FastAPI

from .api import ping, notes
from .db import database, engine, metadata

metadata.create_all(engine)

backend = FastAPI()


@backend.on_event("startup")
async def startup():
    await database.connect()


@backend.on_event("shutdown")
async def shutdown():
    await database.disconnect()


backend.include_router(ping.router)
backend.include_router(notes.router, prefix="/notes", tags=["notes"])
