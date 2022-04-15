from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    name = "Fazlullah Bokhari"
    letters = list(name)
    return render_template('basic.html', my_name = name, my_name_letters = letters)


if __name__ == '__main__':
    app.run(debug=True)