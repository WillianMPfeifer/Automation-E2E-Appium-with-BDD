from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from tests.config.capabilities import Capabilities
from tests.config.settings import Settings
import os


def before_scenario(context, scenario):
    print(f"\n📱 Iniciando cenário: {scenario.name}")

    print(f"📂 Caminho do APK Android: {Settings.ANDROID_APP_PATH}")
    print(f"✅ Arquivo existe? {os.path.exists(Settings.ANDROID_APP_PATH)}")

    platform = Settings.PLATFORM.lower()

    if platform == 'android':
        caps = Capabilities.android_capabilities()
        options = UiAutomator2Options().load_capabilities(caps)

        print(f"📂 Caminho do APK Android: {Settings.ANDROID_APP_PATH}")
        print(f"✅ Arquivo existe? {os.path.exists(Settings.ANDROID_APP_PATH)}")

    elif platform == 'ios':
        caps = Capabilities.ios_capabilities()
        options = XCUITestOptions().load_capabilities(caps)

        print(f"📂 Caminho do APP IOS: {Settings.IOS_APP_PATH}")
        print(f"✅ Arquivo existe? {os.path.exists(Settings.IOS_APP_PATH)}")

    else:
        raise ValueError(f"Plataforma não suportada: {platform}")

    context.driver = webdriver.Remote(
        Settings.APPIUM_SERVER,
        options=options
    )

    context.driver.implicitly_wait(Settings.IMPLICIT_WAIT)
