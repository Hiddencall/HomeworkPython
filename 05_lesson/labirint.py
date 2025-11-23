#  зайти на лабиринт
#  найти книги по слову "Python"
#  Посчитать количество книг по теме Python
#  Вывести в консоль информацию по каждой книге (название, автор, цена).

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

#  зайти на лабиринт
driver.get("https://www.labirint.ru/")

#  найти книги по слову "Python"
search_input = driver.find_element(By.CSS_SELECTOR, "#search-field")
search_input.send_keys('Python', Keys.RETURN)
sleep(5)
#  Посчитать количество книг по теме Python
books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")

#  Вывести в консоль информацию по каждой книге (название, автор, цена).
for book in books:
    author = ''
    name_book = ''
    price_book = ''
    try:
        author = book.find_element(By.CSS_SELECTOR,
                                   "div.product-card__author").text
    except:
        author = "Автор не указан"
    name_book = book.find_element(By.CSS_SELECTOR, ".product-card__name").text
    price_book = book.find_element(By.CSS_SELECTOR,
                                   "div.product-card__price-current").text

    print(f"{name_book}     {author}    {price_book}")
# sleep(5)
