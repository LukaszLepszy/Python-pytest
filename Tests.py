import time
from telnetlib import EC

from selenium.webdriver.common.by import By

from TestBaseClass import TestBaseClass
REGULAR_APP_EXERCISE = "a[class='button'][ data-action ='bugfree']"
ZADANIE_1 = "//h2[text()='Zadanie 1']"
OKULARY = ":first-child input[type='number'] "
ZAD_1 = "a[href='/task_1']"
ADD_BUTTON = "button[id='add-product-60a93cf5bf479']"

class Tests(TestBaseClass):

    def go_to_exercises(self):
        self.driver.get('http://asta.pgs-soft.com/')
        self.driver.find_element_by_css_selector(REGULAR_APP_EXERCISE).click()
        time.sleep(3)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        self.url_exercise_list = self.driver.current_url
        return self.driver, self.url_exercise_list

    def task_1(self, driver):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ZAD_1)))
        self.driver.find_element_by_css_selector(ZAD_1).click()
        return self.driver

    def task_1_add_product(self, driver):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, OKULARY)))
        self.driver.find_element_by_css_selector(OKULARY).clear()
        self.driver.find_element_by_css_selector(OKULARY).send_keys(3)
        self.driver.find_element_by_css_selector(ADD_BUTTON)
        return self.driver
