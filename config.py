import pydantic_settings
from dotenv import load_dotenv


class Config(pydantic_settings.BaseSettings):
    BASE_URL: str = 'https://mamago.by'
    WINDOW_WIDTH: int = 1896
    WINDOW_HEIGHT: int = 1096


load_dotenv()
config = Config()