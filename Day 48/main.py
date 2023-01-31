from selenium.webdriver.common.by import By
from selenium import webdriver

#this driver.exe depent on your chrome version
chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

# driver.get("https://www.amazon.es/dp/B08Z3BQYM1/ref=pd_rhf_d_ee_s_bmx_gp_u625ip4n_sccl_1_3/260-2178921-5444059?content-id=amzn1.sym.18f82f3e-de7c-4b58-b272-7d191cdac7d3&psc=1")
# price = driver.find_element(By.ID,"corePriceDisplay_desktop_feature_div")
# print(price.text)

driver.get("https://www.python.org/")

# element = driver.find_element(By.NAME,"q")
# print(element.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME,"python-logo")
# print(logo.size)

# documentation = driver.find_element(By.CSS_SELECTOR,".documentation-widget a")
# print(documentation.text)

# bug_link = driver.find_element(By.XPATH,"//*[@id='site-map']/div[2]/div/ul/li[3]/a")
# print(bug_link.text)

# anchors = driver.find_elements(By.TAG_NAME,"a")
# print(len(anchors))

# upcoming_date = driver.find_elements(By.CSS_SELECTOR,".event-widget.last > div > ul > li > time")
# upcoming_event = driver.find_elements(By.CSS_SELECTOR,".event-widget.last > div > ul > li > a")

# events = {}
# for x in range(len(upcoming_date)):
#     events[x] = {
#         "time" : upcoming_date[x].get_attribute("datetime").split("T")[0],  
#         "name" : upcoming_event[x].text
#         }


# print(events)


#driver.close()
driver.quit()
