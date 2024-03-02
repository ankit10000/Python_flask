from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello my first project in python'

@app.route('/<name>')
def print_name(name):
    return 'error on page {}'.format(name)

if __name__ == '__main__':
    app.run(debug=True)