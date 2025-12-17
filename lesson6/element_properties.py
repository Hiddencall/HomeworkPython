from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
# driver.get("https://ya.ru")
usd = driver.find_element(By.CSS_SELECTOR,
                         'a[data-statlog="2informers.stocks.item.1"]')

# txt = usd.text
# tag = usd.tag_name
# id = usd.id
# href = usd.get_attribute('href')
# ff = usd.value_of_css_property('font-family')
# color = usd.value_of_css_property('color')


# print(txt)
# print(tag)
# print(id)
# print(href)
# print(ff)
# print(color)

# driver.get("http://uitestingplayground.com/visibility")
# in_display = driver.find_element(By.CSS_SELECTOR,
#                                 "#transparentButton").is_displayed()
# print(in_display)
# sleep(3)
# driver.find_element(By.CSS_SELECTOR, "#hideButton").click()
# in_display = driver.find_element(By.CSS_SELECTOR,
#                                 "#transparentButton").is_displayed()
# print(in_display)
# sleep(3)

# driver.get('https://demoqa.com/radio-button')
# is_enabled = driver.find_element(By.CSS_SELECTOR, '#yesRadio').is_enabled()
# print(is_enabled)
# is_enabled = driver.find_element(By.CSS_SELECTOR, '#noRadio').is_enabled()
# print(is_enabled)

driver.get('https://the-internet.herokuapp.com/checkboxes')
sleep(2)
cb = driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
active = cb.is_selected()
print(active)
sleep(2)
cb.click()
active = cb.is_selected()
print(active)
sleep(2)
driver.quit
