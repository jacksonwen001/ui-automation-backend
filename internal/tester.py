from selenium.webdriver.common.by import By
from .operations import Operation

from .browser import Browser

class Tester:
    def __init__(self) -> None:
        self.browser: Browser = None
        self.operation: Operation = None
        self.browsers = {
            'chrome': lambda version: self.browser.start_chrome(version), 
            'firefox': lambda version: self.browser.start_firefox(version), 
            'edge': lambda version: self.browser.start_edge(version)
        }

        self.operations = {
            'open': lambda selector, target, value, datasource: self.operation.open(value), 
            'click': lambda selector, target, value, datasource: self.operation.click(selector, target),
            'click_at': lambda selector, target, value, datasource: self.operation.click_at(selector, target),
            'move_to_click': lambda selector, target, value, datasource: self.operation.move_to_click(selector, target), 
            'type': lambda selector, target, value, datasource: self.operation.type(selector, target, value), 
            'sleep': lambda selector, target, value, datasource: self.operation.sleep(value)
        }
        
    def start_browser(self, browser: str, version: str):
        self.browser = Browser()
        self.browsers[browser](version)
        self.operation = Operation(self.browser.driver)

    
    def execute(self, command: str, selector: str = None, target: str = None, value: str = None, datasource: dict = None): 
        self.operations[command](selector, target, value, datasource)
    
    def quit(self):
        self.browser.quit()
    

   

    
        
    

    
