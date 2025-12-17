from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
driver.get("https://google.com")

element = driver.find_element(By.CSS_SELECTOR, '[title]')
element.clear()
element.send_keys('Звёздные войны')
sleep(5)
driver.find_element(By.CSS_SELECTOR, 'input.gNO89b').click()
sleep(5)
