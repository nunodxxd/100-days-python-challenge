from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

def logging_decorator(function):
    def wrapper():
        print(f"You called {function.__name__} function")
        print(f"{function.__name__} returned: {function()}")
        return function()
    return wrapper

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center"> Hello, World! </h1>' \
            '<p>This is a paragraph.</p>' \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>'

@app.route('/<name>/<int:number>')
def greet(name,number):
    return f"Hello {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)