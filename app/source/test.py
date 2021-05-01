from datetime import datetime as dt
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1280,1024")

driver = webdriver.Remote(
    command_executor=os.environ["SELENIUM_URL"],
    desired_capabilities=DesiredCapabilities.FIREFOX.copy()
)
driver.get("https://www.nict.go.jp/JST/JST5.html")

driver.implicitly_wait(3)
sleep(1)

driver.save_screenshot("{0:%Y_%m_%d__%H_%M_%S}".format(dt.now()) + ".png")

driver.quit()