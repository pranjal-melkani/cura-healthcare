from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class Basedriver:
    def __init__(self, driver):
        self.driver = driver

    def wait_until_element_is_visible(self, xpath):
        # timeout = config.get('DEFAULT', 'timeout')
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return element

    def click_on_element(self, xpath):
        element = self.wait_until_element_is_visible(xpath)
        element.click()

    def send_keys(self, xpath, key_input):
        element = self.wait_until_element_is_visible(xpath)
        element.send_keys(key_input)

    def select_dropdown(self, xpath, visible_text):
        element = self.wait_until_element_is_visible(xpath)
        Select(element).select_by_visible_text(visible_text)
