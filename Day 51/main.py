from internet import InternetSpeedTwitterBot

CHROME_DRIVER_PATH = "./chromedriver.exe"
TWITTER_EMAIL = ""
TWITTER_NAME = ""
TWITTER_PASSWORD = ""

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if int(bot.d_speed) < 1000 or int(bot.u_speed) < 200:
    bot.tweet_at_provider(TWITTER_EMAIL,TWITTER_NAME,TWITTER_PASSWORD)
