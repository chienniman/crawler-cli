import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options=Options()
options.chrome_executable_path="chromedriver.exe"
driver=webdriver.Chrome(options=options)
driver.get("https://ani.gamer.com.tw/")

button = driver.find_element(By.CSS_SELECTOR, ".anime-btn-show-more") 
button.click()

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f"anime_data_{timestamp}.txt"

with open(file_name, "w",encoding="utf-8") as file:
    file.write("")
data = []

elements = driver.find_elements(By.CSS_SELECTOR, ".newanime-block .anime-name p:first-child")
for index,element in enumerate(elements):
    if element.text:
        data.append(f"[{index + 1}]: {element.text}")
        print(f"[{index + 1}]: {element.text}")

with open(file_name, "a", encoding="utf-8") as file:
    for item in data:
        file.write(item + "\n")

driver.close()