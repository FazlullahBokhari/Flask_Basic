from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    userlogin = False
    name = "Fazlullah Bokhari"
    letters = list(name)
    mylist = [10,20,30,400,50,60]
    return render_template('basic.html', my_name = name, my_name_letters = letters,numeric_list = mylist,user_status = userlogin)


if __name__ == '__main__':
    app.run(debug=True)