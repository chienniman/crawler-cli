from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options=Options()
options.chrome_executable_path="chromedriver.exe"

driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://ani.gamer.com.tw/")
driver.save_screenshot("screenshot.png")
driver.close()