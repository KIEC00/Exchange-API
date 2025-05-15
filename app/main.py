from fastapi import FastAPI
import uvicorn

from app.core import config

app = FastAPI()


def main() -> None:
    uvicorn.run(
        "app.main:app",
        host=config.run.host,
        port=config.run.port,
        reload=config.run.reload,
    )


if __name__ == "__main__":
    main()
