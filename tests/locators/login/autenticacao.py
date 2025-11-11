from appium.webdriver.common.appiumby import AppiumBy

class LoginLocators:

    ACCEPT_TERMS_CHECKBOX = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"uncheckedIcon\")")
    ACCEPT_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"ACEITAR\")")
    CPF_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Informe seu CPF ou CNPJ")
    PASSWORD_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Informe sua senha")
    LOGIN_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"ENTRAR\")")
    ERROR_MESSAGE = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.FrameLayout\").instance(0)")
    CONTINUE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Avançar\")")
    HOME_SCREEN_IDENTIFIER = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Selecione a turma que você deseja gerenciar\")")