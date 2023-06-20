from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = input("Please enter the URL of the webpage: ")

options=Options()
options.chrome_executable_path="chromedriver.exe"

driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(url)
driver.save_screenshot("screenshot.png")
driver.close()