from follower import InstaFollower

chrome_driver_path = "./chromedriver.exe"

USERNAME = "username"
PASSWORD = "password"
ACCOUNT = "account"

insta = InstaFollower(chrome_driver_path)
insta.login(USERNAME,PASSWORD)
insta.find_followers(ACCOUNT)
insta.follow()