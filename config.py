import pydantic_settings
from dotenv import load_dotenv


class Config(pydantic_settings.BaseSettings):
    BASE_URL: str = 'https://mamago.by'
    WINDOW_WIDTH: int = 1896
    WINDOW_HEIGHT: int = 1096
    USER_NAME: str = 'yarutich.irina'
    LOGIN_USERNAME: str = 'yarutich.irina@gmail.com'
    LOGIN_PASSWORD: str = '150424mg'


load_dotenv()
config = Config()