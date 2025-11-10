from appium import webdriver
from appium.options.android import UiAutomator2Options
from tests.config.capabilities import Capabilities
from tests.config.settings import Settings
# from appium.options.ios import XCUITestOptions  # se for usar iOS no futuro

def before_scenario(context, scenario):
    print(f"\n📱 Iniciando cenário: {scenario.name}")

    platform = Settings.PLATFORM.lower()

    if platform == 'android':
        caps = Capabilities.android_capabilities()
        options = UiAutomator2Options().load_capabilities(caps)

    # elif platform == 'ios':
    #     caps = Capabilities.ios_capabilities()
    #     options = XCUITestOptions().load_capabilities(caps)

    else:
        raise ValueError(f"Plataforma não suportada: {platform}")

    # ✅ Novo formato Appium 3.x
    context.driver = webdriver.Remote(
        Settings.APPIUM_SERVER,
        options=options
    )

    context.driver.implicitly_wait(Settings.IMPLICIT_WAIT)
