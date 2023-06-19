from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

'''
title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present
'''
class Browser:
    def __init__(self):
        # remote url
        self.__selenoid_url = "http://20.253.96.68:4444/wd/hub"
        # webdriver
        self.driver: webdriver = None
        self.browsers = {
            'chrome': ChromeOptions(), 
            'firefox': FirefoxOptions(), 
            'edge': EdgeOptions()
        }
    
    def __start_browser(self, browser: str, version: str): 
        options = self.browsers[browser]
        options.browser_version = version
        options.set_capability("selenoid:options", {
            "enableVideo": True, 
            "enableVNC": True
        })
        self.driver = webdriver.Remote(command_executor=self.__selenoid_url, options=options)
    
    def start_chrome(self, version: str):
        self.__start_browser('chrome', version)
    
    def start_firefox(self, version: str):
        self.__start_browser('firefox', version)

    def start_edge(self, version: str):
        self.__start_browser('msedge', version)

    def start_safari(self, version: str):
         self.__start_browser('safari', version)
    
    def get_session_id(self):
        return self.driver.session_id
    
    def quit(self):
        self.driver.quit()