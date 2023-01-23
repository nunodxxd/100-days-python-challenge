########################### EMAIL VERSION ############################
import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

load_dotenv()


email_sender = os.getenv('EMAIL_SENDER')
email_passowrd = os.getenv('EMAIL_PASSWORD')
email_receiver = os.getenv('EMAIL_RECEIVER')

class NotificationManager:

    def __init__(self):
        self.sender = email_sender
        self.password = email_passowrd
        self.receiver = email_receiver
        
    def send_email(self,flight_data,emails=[]):
        title = f"Low price alert to {flight_data.destination_city}!"
        #replace the link to google search bc google flights not work
        link = f"https://www.google.com/search?q={flight_data.origin_city}-{flight_data.origin_airport}+to+{flight_data.destination_city}-{flight_data.destination_airport}+from+{flight_data.out_date}+to+{flight_data.return_date}"
        body = f"Only {flight_data.price}€ to fly from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport}, from {flight_data.out_date} to {flight_data.return_date}. \n{link}"
        if flight_data.stop_overs > 0:
            body = f"Low price alert! Only {flight_data.price}€ to fly from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport}, from {flight_data.out_date} to {flight_data.return_date} with {flight_data.stop_overs} stop over(s) in {flight_data.via_city}. \n{link}"
    
        if len(emails) > 0:
            for email in emails:
                em = EmailMessage()
                em['Subject'] = title
                em['From'] = email_sender
                em['To'] = email
                em.set_content(body)
                
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
                    server.login(email_sender, email_passowrd)
                    server.sendmail(email_sender, email_receiver, em.as_string())
        else:
            em = EmailMessage()
            em['Subject'] = title
            em['From'] = email_sender
            em['To'] = email_receiver
            em.set_content(body)
            
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
                server.login(email_sender, email_passowrd)
                server.sendmail(email_sender, email_receiver, em.as_string())


########################### TWILIO VERSION ############################
# from twilio.rest import Client

# ACCOUNT_SID = "---"
# AUTH_TOKEN = "----"
# FROM = "----"
# TO = "-----"

# class NotificationManager:
#     def __init__(self):
#         self.account_sid = ACCOUNT_SID
#         self.auth_token = AUTH_TOKEN
#         self.client = Client(self.account_sid, self.auth_token)
        
#     def send_sms(self, flight_data):
#         content = f"Low price alert! Only {flight_data.price}€ to fly from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport}, from {flight_data.out_date} to {flight_data.return_date}."
#         message = self.client.messages \
#             .create(
#                 body=content,
#                 from_=FROM,
#                 to=TO
#             )
#         print(message.status)