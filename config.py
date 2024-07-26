from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    class Config:
        env_file:str ='.env'
        
       
@lru_cache 
def get_settings()->Settings:
    return Settings()