from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 3000
    # class Config:
    #     env_file = "../.env"


settings = Settings(
    _env_file='../.env',
    _env_file_encoding='utf-8'
)
