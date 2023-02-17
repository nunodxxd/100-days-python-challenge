from flask import Flask, render_template
from form import LoginForm
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()
app.secret_key = "some secret string"

# Create a fake user database
ADMIN = "admin@email.com"
ADMIN_PASSWORD = "12345678"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login" , methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == ADMIN and form.password.data == ADMIN_PASSWORD:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)