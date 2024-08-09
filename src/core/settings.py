from pydantic import ConfigDict
from pydantic_settings import BaseSettings

class DBConfig(BaseSettings):
    host: str
    port: str
    user: str
    password: str
    name: str

    class Config:
        env_prefix = "DB_"
        env_file = '.env'
        extra = 'ignore'


    @property
    def dsn(self):
        print(f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}")
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class Settings(BaseSettings):
    db: DBConfig


def get_settings():
    return Settings(
        db=DBConfig()
    )
