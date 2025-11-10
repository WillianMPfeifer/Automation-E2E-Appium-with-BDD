from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# Pesquisar esses imports depois
from tests.config.settings import Settings
from datetime import datetime

class CommonFunctions:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Settings.EXPLICIT_WAIT)
    
    def encontrar_elemento(self, locator, timeout=None):
        wait_time = timeout if timeout else Settings.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.presence_of_element_located(locator))
    
    def encontrar_elementos(self, locator, timeout=None):
        wait_time = timeout if timeout else Settings.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.presence_of_all_elements_located(locator))
    
    def clicar(self, locator, timeout=None):
        wait_time = timeout if timeout else Settings.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        element = wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def digitar(self, locator, text, clear_first=True):
        element = self.encontrar_elemento(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)
    
    def obter_texto(self, locator):
        element = self.encontrar_elemento(locator)
        return element.text
    
    def elemento_eh_visivel(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def elemento_eh_presente(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def aguarda_elemento_desaparecer(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def rolar_ate_elemento(self, locator):
        element = self.encontrar_elemento(locator)
        self.driver.execute_script("mobile: scrollToElement", {"elementId": element.id})
    
    def deslizar_para_cima(self, duration=800):
        size = self.driver.get_window_size()
        start_x = size['width'] // 2
        start_y = size['height'] * 0.8
        end_y = size['height'] * 0.2
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)
    
    def deslizar_para_baixo(self, duration=800):
        size = self.driver.get_window_size()
        start_x = size['width'] // 2
        start_y = size['height'] * 0.2
        end_y = size['height'] * 0.8
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)
    
    def capturar_screenshot(self, name):
        Settings.ensure_directories()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo = f"{name}_{timestamp}.png"
        caminho_arquivo = Settings.SCREENSHOTS_DIR / nome_arquivo
        self.driver.save_screenshot(str(caminho_arquivo))
        return str(caminho_arquivo)
    
    def esconder_teclado(self):
        try:
            self.driver.hide_keyboard()
        except:
            pass 