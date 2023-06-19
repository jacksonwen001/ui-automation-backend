from tester import Tester

if __name__ == "__main__":
    tester = Tester()
    tester.start_browser('chrome', '110.0')
    tester.execute('open', value="https://www.google.com")
    tester.execute('type', selector='css', target='textarea[name="q"]', value='selenium')
    tester.quit()