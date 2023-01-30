import requests
import bs4
from email.message import EmailMessage
import ssl
import smtplib

#amazon product url
url = "https://www.amazon.es/dp/B08Z3BQYM1/ref=pd_rhf_d_ee_s_bmx_gp_u625ip4n_sccl_1_3/260-2178921-5444059?content-id=amzn1.sym.18f82f3e-de7c-4b58-b272-7d191cdac7d3&psc=1"

# headers ("some":"nonsense" is to bypass 503 error)
# scraping amazon is not allowed, so we need to use headers to bypass the security but only for testing porpuses
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "some": "nonsense"
}

# get the data from the website
response = requests.get(url=url, headers=headers)
response.raise_for_status()
print(response.text)

# scrape the data from the website
soup = bs4.BeautifulSoup(response.text, "html.parser")
name = soup.select_one(selector="#productTitle").get_text().strip()
price = soup.select_one(selector="#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center > span > span.a-offscreen").get_text().replace("€", "")

price_alert = 35

# less secure apps don't work anymore, so we need to create an app password 
# use this link: https://myaccount.google.com/u/3/apppasswords
# and select "Mail" and "Other" and give a name to the app
if float(price) < price_alert:
    # send email
    email_sender = "emai_sender"
    email_passowrd = "password"
    email_receiver = "email_receiver"

    title = f"Low price alert to amazon product!"
    body = f"Only {price}€ to buy {name}"


    em = EmailMessage()
    em['Subject'] = title
    em['From'] = email_sender
    em['To'] = email_receiver
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(email_sender, email_passowrd)
    server.sendmail(email_sender, email_receiver, em.as_string())