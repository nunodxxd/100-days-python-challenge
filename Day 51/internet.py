from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PROMISSED_DOWN = 1000
PROMISSED_UP = 200

class InternetSpeedTwitterBot():
    def __init__(self,):
        self.bot = webdriver.Chrome()

    def get_internet_speed(self):
        bot = self.bot
        bot.get("https://www.speedtest.net/")
        go_button = bot.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()
        time.sleep(60)
        download_speed = bot.find_element(By.CSS_SELECTOR, ".download-speed")
        upload_speed = bot.find_element(By.CSS_SELECTOR, ".upload-speed")
        self.d_speed = download_speed.text
        self.u_speed = upload_speed.text

    def tweet_at_provider(self,email,username,password):
        bot = self.bot
        bot.get("https://twitter.com/i/flow/login")
        time.sleep(2)
        element_email = bot.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        element_email.send_keys(email)
        element_email.send_keys(Keys.RETURN)
        time.sleep(2)
        element_username = bot.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
        element_username.send_keys(username)
        element_username.send_keys(Keys.RETURN)
        time.sleep(2)
        element_password = bot.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        element_password.send_keys(password)
        element_password.send_keys(Keys.RETURN)
        time.sleep(2)
        tweet = bot.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div")
        tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.d_speed}down/{self.u_speed}up when I pay for {PROMISSED_DOWN}down/{PROMISSED_UP}up?")
        tweet.send_keys(Keys.RETURN)
        time.sleep(2)
        bot.quit()
        

