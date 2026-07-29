from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, computed_field
from sqlalchemy import URL
from pathlib import Path
import os

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = Path(ROOT_DIR, ".env")


class SettingsSystem(BaseSettings):
    """
    System settings class.
    """
    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        extra="ignore",
        env_prefix='SYSTEM_'
    )

    debug: bool = True
    secret_key: str = ""
    algorithm: str = "HS256"
    token_expiration_minutes: int = 60
    time_zone: str = "Europe/Kyiv"


class DBSettings(BaseSettings):
    """
    DB settings class.
    """
    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        extra="ignore",
        env_prefix='DB_'
    )

    drivername: str = "sqlite"
    username: str = ""
    password: str = ""
    host: str = ""
    port: int | None = None
    database: str = ""

    @computed_field
    @property
    def url_object(self) -> URL:
         return URL.create(
            drivername=self.drivername,
            username=self.username,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database
        )


class Config(BaseSettings):
    """
    Main config class.
    """
    system_settings: SettingsSystem = Field(default_factory=SettingsSystem)
    db_settings: DBSettings = Field(default_factory=DBSettings)

    @classmethod
    def load(cls) -> "Config":
        return cls()

config = Config.load()
