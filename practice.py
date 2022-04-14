from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def translate(name):
    if name[len(name)-1] == "y":
        name = name[0:len(name)-1] + "iful"
        return "<h1> This is a {}</h1>".format(name.title())
    else:
        name = name+"y"
        return "<h1> This is a {}</h1>".format(name.title())

if __name__ == "__main__":
    app.run(debug=True)