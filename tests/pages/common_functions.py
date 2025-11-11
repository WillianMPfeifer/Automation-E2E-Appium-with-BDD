from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from tests.config.settings import Settings
from datetime import datetime

class CommonFunctions:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Settings.EXPLICIT_WAIT)
    
    def find_element(self, locator, timeout=None):
        wait_time = timeout if timeout else Settings.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator, timeout=None):
        wait_time = timeout if timeout else Settings.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.presence_of_all_elements_located(locator))
    
    def click(self, locator, timeout=None):
        wait_time = timeout if timeout else Settings.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        element = wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def send_keys(self, locator, text, clear_first=True):
        element = self.find_element(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
    
    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def is_element_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def wait_for_element_to_disappear(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("mobile: scrollToElement", {"elementId": element.id})
    
    def swipe_up(self, duration=800):
        size = self.driver.get_window_size()
        start_x = size['width'] // 2
        start_y = size['height'] * 0.8
        end_y = size['height'] * 0.2
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)
    
    def swipe_down(self, duration=800):
        size = self.driver.get_window_size()
        start_x = size['width'] // 2
        start_y = size['height'] * 0.2
        end_y = size['height'] * 0.8
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)
    
    def capture_screenshot(self, name):
        Settings.ensure_directories()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{name}_{timestamp}.png"
        file_path = Settings.SCREENSHOTS_DIR / file_name
        self.driver.save_screenshot(str(file_path))
        return str(file_path)
    
    def hide_keyboard(self):
        try:
            self.driver.hide_keyboard()
        except:
            pass 