from tests.config.settings import Settings

class Capabilities:
    """Desired Capabilities para diferentes dispositivos"""
    
    @staticmethod
    def android_capabilities():
        """Capabilities para Android"""
        return {
            "appium:automationName": "uiautomator2",
            "appium:deviceName": "Medium Phone",
            "appium:app": "G:\\Meu Drive\\TESTES\\DDF APP\\Versão nova 2.8 Educação\\DDF-2313 (Botões flutuantes)\\DDF-2315.apk",
            "appium:platformVersion": "11.0",
            "appium:newCommandTimeout": 0,
            "platformName": "Android"
    }
    
    # @staticmethod
    # def ios_capabilities():
    #     """Capabilities para iOS"""
    #     return {
    #         "platformName": "iOS",
    #         "platformVersion": "16.0",
    #         "deviceName": "iPhone 14",
    #         "automationName": "XCUITest",
    #         "app": Settings.IOS_APP_PATH,
    #         "bundleId": "br.gov.digipaisealunos",  # Ajustar conforme seu app
    #         "noReset": False,
    #         "fullReset": False,
    #         "newCommandTimeout": 300
    #     }