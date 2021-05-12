
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
from time import sleep

driver = webdriver.Remote(
    command_executor=os.environ["SELENIUM_URL"],
    desired_capabilities=DesiredCapabilities.FIREFOX.copy()
)

search_url = 'https://chiebukuro.yahoo.co.jp/'
driver.get(search_url)

driver.close()