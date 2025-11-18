from selenium import webdriver

class webDriverManager:
    def __init__(self):
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--headless")  # Run in headless mode
        self.driver = webdriver.Chrome(options=chromeOptions)
        print("Web driver initialized successfully.")
    
    def getDriver(self):
        return self.driver
    
    def closeDriver(self):
        self.driver.quit()
        print("Web driver closed successfully.")
        