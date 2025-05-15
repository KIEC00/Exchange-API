from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

from app.core import config, db
from app.models.base import BaseORM


@asynccontextmanager
async def lifespan(app: FastAPI):
    # TODO: remove and make migrations
    async with db.engine.begin() as conn:
        await conn.run_sync(BaseORM.metadata.create_all)
    # /TODO: remove and make migrations
    yield
    await db.dispose()


app = FastAPI(lifespan=lifespan)


def main() -> None:
    uvicorn.run(
        "app.main:app",
        host=config.run.host,
        port=config.run.port,
        reload=config.run.reload,
    )


if __name__ == "__main__":
    main()
