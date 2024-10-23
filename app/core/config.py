from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = "sqlite+aiosqlite:///database/database.db"
    test_db_url: str = "sqlite+aiosqlite:///:memory:"
    is_test: bool = False

    def test_mode(self):
        settings.is_test = True
        settings.db_url = self.test_db_url


settings = Settings()

settings.test_mode()
