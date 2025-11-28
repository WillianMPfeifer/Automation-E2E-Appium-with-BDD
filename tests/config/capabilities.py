from tests.config.settings import Settings

class Capabilities:
    
    @staticmethod
    def android_capabilities():
        return {
            "appium:automationName": "uiautomator2",
            "appium:deviceName": "Medium Phone",
            "appium:udid": "emulator-5554",
            "appium:app": Settings.ANDROID_APP_PATH,
            "appium:platformVersion": "11.0",
            "appium:newCommandTimeout": 0,
            "appium:autoGrantPermissions": True,
            "platformName": "Android"
    }
    
    @staticmethod
    def ios_capabilities():
        return {
            "platformName": "iOS",
            "platformVersion": "16.0",
            "deviceName": "iPhone 14",
            "automationName": "XCUITest",
            "app": Settings.IOS_APP_PATH,
            "bundleId": "br.gov.digipaisealunos",
            "noReset": False,
            "fullReset": False,
            "newCommandTimeout": 300
        }