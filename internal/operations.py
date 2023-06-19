import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

class Operation():
    def __init__(self, driver: webdriver) -> None:
        self.element: WebElement = None
        self.selectors: dict = {
            'xpath':     By.XPATH, 
            'css':       By.CSS_SELECTOR, 
            'className': By.CLASS_NAME, 
            'id':        By.ID, 
            'name':      By.NAME
        }

        self.driver = driver
        self.duration = 20
        
    def open(self, url: str): 
        try:
            self.driver.get(url)
        except Exception as e:
            print('open error! value: {}, exception: {}'.format(url, e))


    def click(self, selector: str, target: str): 
        by: By = self.selectors[selector]
        try:
            self.wait_for_clickable(by, target).click()
        except:
            print('click error! selector: {}, target: {}'.format(selector, target))

    def sleep(self, value: str):
        try:
            time.sleep(int(value))
        except Exception as e:
            print('sleep error! value: {}, exception:{}'.format(value, e))

    def click_at(self, selector: str, target: str):
        try:
            self.visibility(self.selectors[selector], target).click()
        except Exception as e: 
            print('click_at error! selector: {}, target: {}, exception: {}'.format(selector, target, e))

    def move_to_click(self, selector: str, target: str):
        action = ActionChains(self.driver)
        try:
            action.move_to_element(self.visibility(self.selectors[selector], target)).click().perform()
        except Exception as e:
            print('move_to_click error! selector: {}, target: {}, exception: {}'.format(selector, target, e))

    def type(self, selector: str, target: str = None, value: str=None):        
        try: 
            self.presence(self.selectors[selector], target).send_keys(value)
        except Exception as e:
            print('type error! selector: {}, target: {},value:{} exception: {}'.format(selector, target, value, e))
        
    def presence(self, by: By, element: str) -> WebElement:
        return WebDriverWait(self.driver, self.duration).until(EC.presence_of_element_located((by, element))) 
    
    def visibility(self, by: By, element: str) -> WebElement:
        return WebDriverWait(self.driver, self.duration).until(EC.visibility_of_element_located((by, element)))
        
    def invisibility(self, by: By, element: str) -> visibility:
        return WebDriverWait(self.driver, self.duration).until(EC.invisibility_of_element_located((by, element)))
        
    def wait_for_clickable(self, element: WebElement) -> WebElement:
        return WebDriverWait(self.driver, self.duration).until(EC.element_to_be_clickable(element))
         
    def wait_for_clickable(self, by: By, element: str) -> WebElement:
        return WebDriverWait(self.driver, self.duration).until(EC.element_to_be_clickable((by, element)))

    def is_contains(self, by: By, element: str, text:str) -> bool:
        return WebDriverWait(self.driver, self.duration).until(EC.text_to_be_present_in_element((by, element), text))
        
    def has_attribute(self, by: By, element: str, attr: str, text:str) -> bool:
        return WebDriverWait(self.driver, self.duration).until(EC.text_to_be_present_in_element_attribute((by, element), attr, text))