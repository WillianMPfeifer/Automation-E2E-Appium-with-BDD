# tests/utils/driver_factory.py
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from tests.config.capabilities import Capabilities
from tests.config.settings import Settings
import os

class DriverFactory:
    @staticmethod
    def get_driver(logger):
  
        platform = Settings.PLATFORM.lower()
        options = None

        if platform == 'android':
            caps = Capabilities.android_capabilities()
            options = UiAutomator2Options().load_capabilities(caps)
            
            if not os.path.exists(Settings.ANDROID_APP_PATH):
                logger.error(f"❌ APK não encontrado em: {Settings.ANDROID_APP_PATH}")
                raise FileNotFoundError(f"APK não encontrado: {Settings.ANDROID_APP_PATH}")
                
        elif platform == 'ios':
            caps = Capabilities.ios_capabilities()
            options = XCUITestOptions().load_capabilities(caps)
            
            if not os.path.exists(Settings.IOS_APP_PATH):
                logger.error(f"❌ APP iOS não encontrado em: {Settings.IOS_APP_PATH}")
                raise FileNotFoundError(f"APP iOS não encontrado: {Settings.IOS_APP_PATH}")
        else:
            raise ValueError(f"Plataforma não suportada: {platform}")

        try:
            driver = webdriver.Remote(Settings.APPIUM_SERVER, options=options)
            driver.implicitly_wait(Settings.IMPLICIT_WAIT)
            return driver
        except Exception as e:
            logger.error(f"❌ Falha crítica ao conectar no Appium Server: {e}")
            raise e