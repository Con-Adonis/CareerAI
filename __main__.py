import os
import sys
from src.scraping.webdriver import webDriverManager
import user.installerPages as installerPages

def main():
    #welcome screen/ setup wizard, comment line below to remove initialization process
    installerPages.main()
    
    #establish web driver
    manager = webDriverManager()
    driver = manager.getDriver()
    
    #closing driver
    manager.closeDriver()


if __name__ == "__main__":
    main()
    