from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)


driver.get("https://www.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# all portals don't exist in the page i change it for another element
# other_wiki = driver.find_element(By.LINK_TEXT, "other Wikipedias are available")
# other_wiki.click()

# search = driver.find_element(By.CSS_SELECTOR, "#searchform > div > div > div.cdx-text-input.cdx-text-input--has-start-icon.cdx-search-input__text-input > input")
# search.send_keys("Python")
# button = driver.find_element(By.CSS_SELECTOR, "#searchform > div > button")
# button.click()