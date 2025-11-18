import os
import sys
from src.scraping.webdriver import webDriverManager
import src.user.welcome as welcome

def main():
    #welcome screen/ setup wizard
    #welcome.main()
    
    #establish web driver
    manager = webDriverManager()
    driver = manager.getDriver()
    
    #closing driver
    manager.closeDriver()


if __name__ == "__main__":
    main()
    