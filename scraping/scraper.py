from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#setting up web driver
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--headless")  # Run in headless mode
driver = webdriver.Chrome(options=chromeOptions)
