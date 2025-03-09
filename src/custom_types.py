"""All custom types are located here."""

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class AppEnvVariables(BaseSettings):
    """The app env vars, with all settings/credentials for:
    - database
    """

    # DATABASE
    db_driver: str
    """Database driver."""

    db_name: str
    """Database name."""

    model_config = ConfigDict(extra="forbid")
    """Model config."""

