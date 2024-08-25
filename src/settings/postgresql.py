from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class PostgresSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="POSTGRES_")
    
    user: str = 'xxx'
    password: SecretStr = 'xxx'
    db: str = 'xxx'
    host: str = 'xxx'