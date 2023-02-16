from flask import Flask, render_template, request
import requests
from email.message import EmailMessage
import ssl
import smtplib

data = requests.get('https://api.npoint.io/cc5f1bcfc4477ba4bb90').json()

OWN_EMAIL = "email"
OWN_PASSWORD = "passowrd"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', posts=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact',  methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template('contact.html' , msg_sent=True)
    return render_template('contact.html', msg_sent=False )

@app.route('/post/<int:index>')
def post(index=None):
    return render_template('post.html', post=data[index-1])

def send_email(name, email, phone, message):
    email_receiver = email

    body = f"New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    
    em = EmailMessage()
    em['Subject'] = f"I Have questions - {name}"
    em['From'] = OWN_EMAIL
    em['To'] = OWN_EMAIL
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(OWN_EMAIL, OWN_PASSWORD)
        server.sendmail(OWN_EMAIL, OWN_EMAIL, em.as_string())
    

if __name__ == '__main__':
    app.run(debug=True)
