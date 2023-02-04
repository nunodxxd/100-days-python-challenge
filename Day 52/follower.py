from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time

class InstaFollower():
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

    def login(self, username, password):
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys(username)
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(3)

    def find_followers(self, account):
        self.driver.get(f"https://www.instagram.com/{account}")
        time.sleep(2)
        followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)
        popup = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()