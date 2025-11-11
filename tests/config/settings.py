import os
from pathlib import Path

class Settings:
    
    ROOT_DIR = Path(__file__).parent.parent.parent
    TESTS_DIR = ROOT_DIR / "tests"
    REPORTS_DIR = ROOT_DIR / "reports"
    SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"
    
    APPIUM_SERVER = os.getenv('APPIUM_SERVER', 'http://localhost:4723')
    
    PLATFORM = os.getenv('PLATFORM', 'Android')
    
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20
    
    ANDROID_APP_PATH = os.path.join(ROOT_DIR,
    os.getenv('ANDROID_APP_PATH', 'apps/android/app.apk')
    )

    IOS_APP_PATH = os.path.join(ROOT_DIR,
    os.getenv('IOS_APP_PATH', 'apps/ios/app.app')
    )
    
    @classmethod
    def ensure_directories(cls):
        cls.SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
        cls.REPORTS_DIR.mkdir(parents=True, exist_ok=True)