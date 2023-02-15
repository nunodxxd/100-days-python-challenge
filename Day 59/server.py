from flask import Flask, render_template 
import requests

data = requests.get('https://api.npoint.io/cc5f1bcfc4477ba4bb90').json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', posts=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:index>')
def post(index=None):
    return render_template('post.html', post=data[index-1])

if __name__ == '__main__':
    app.run(debug=True)
