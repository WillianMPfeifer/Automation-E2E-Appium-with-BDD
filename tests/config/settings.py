import os
from pathlib import Path

class Settings:
    """Configurações globais do projeto"""
    
    # Diretórios
    ROOT_DIR = Path(__file__).parent.parent.parent
    TESTS_DIR = ROOT_DIR / "tests"
    REPORTS_DIR = ROOT_DIR / "reports"
    SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"
    
    # Appium Server
    APPIUM_SERVER = os.getenv('APPIUM_SERVER', 'http://localhost:4723')
    
    # Platform
    PLATFORM = os.getenv('PLATFORM', 'Android')  # Android ou iOS
    
    # Timeouts
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20
    
    # App paths
    ANDROID_APP_PATH = os.getenv('ANDROID_APP_PATH', '/path/to/app.apk')
    # IOS_APP_PATH = os.getenv('IOS_APP_PATH', '/path/to/app.app')
    
    @classmethod
    def ensure_directories(cls):
        """Cria diretórios necessários"""
        cls.SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
        cls.REPORTS_DIR.mkdir(parents=True, exist_ok=True)