from flask import Flask,render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(0,10)
    year = datetime.datetime.now().year
    return render_template('index.html',num=random_number, year=year)

@app.route('/guess/<name>')
def guess(name):
    age = requests.get(f'https://api.agify.io?name={name}').json()['age']
    gender = requests.get(f'https://api.genderize.io/?name={name}').json()['gender']
    return render_template('guess.html',name=name,age=age,gender=gender)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html',posts=all_posts)



if __name__ == "__main__":
    app.run(debug=True)