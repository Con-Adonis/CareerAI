import os
import sys
from src.scraping.webdriver import webDriverManager
import user.installerPages as installerPages
#Demo imports
import src.devTest.applicationDemo as applicationDemo

def main():
    #welcome screen/ setup wizard, comment line below to remove initialization process
    installerPages.main()

    #demo - run devTest logic
    applicationDemo()
    
    '''
    #establish web driver
    manager = webDriverManager()
    driver = manager.getDriver()
    
    #closing driver
    manager.closeDriver()
    '''


if __name__ == "__main__":
    main()
    