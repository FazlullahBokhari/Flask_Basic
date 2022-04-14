from flask import Flask

app = Flask(__name__)


@app.route('/') #127.0.0.1:5000
def index():
    return '<h1> Hello Faiz </h1>'

@app.route('/information') #127.0.0.1:5000/information
def info():
    return "<h1>Flask Lecture for YouTube </h1>"

@app.route('/user/<name>')
def user(name):
    return "<h1>100th This is a page for {}</h1>".format(name.title()[100])





if __name__ == '__main__':
    app.run(debug=True)
