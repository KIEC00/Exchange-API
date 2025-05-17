from pydantic import BaseModel
from pydantic_settings import BaseSettings


class ConfigBase(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        env_nested_delimiter = "__"
        env_prefix = "APP__"
        extra = "ignore"


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = False


class DatabaseConfig(BaseModel):
    driver: str = "postgresql+asyncpg"
    host: str
    port: int
    name: str
    username: str
    password: str
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 20
    max_overflow: int = 20

    @property
    def dsn(self) -> str:
        return f"{self.driver}://{self.username}:{self.password}@{self.host}:{self.port}/{self.name}"


class Config(ConfigBase):
    run: RunConfig
    db: DatabaseConfig


config = Config()  # type: ignore
