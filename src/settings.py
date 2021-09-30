from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 3000
    SQL_DB = 'postgresql://anton:bkZ3qFY2EjfY_EctRE98TMNDxKjNvtcC@130.61.245.101:32372/anton'
    # class Config:
    #     env_file = "../.env"


settings = Settings(
    _env_file='../.env',
    _env_file_encoding='utf-8'
)
