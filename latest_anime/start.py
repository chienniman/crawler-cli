from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options=Options()
options.chrome_executable_path="chromedriver.exe"
driver=webdriver.Chrome(options=options)
driver.get("https://ani.gamer.com.tw/")

button = driver.find_element(By.CSS_SELECTOR, ".anime-btn-show-more") 
button.click()

elements = driver.find_elements(By.CSS_SELECTOR, ".newanime-block .anime-name p:first-child")
for index,element in enumerate(elements):
    if element.text:
        print(f"[{index + 1}]: {element.text}")
driver.close()