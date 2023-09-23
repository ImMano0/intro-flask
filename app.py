from flask import Flask

app = Flask(__name__)


@app.route("/Home/")
def Home():
    return "<h1>Home!</h1>"

@app.route("/Aboute/")
def Aboute():
    return "<h1>Aboute!</h1>"

@app.route("/Contact/")
def Contact():
    return "<h1>Contact!</h1>"

@app.route("/Product/")
def Product():
    return "<h1>Product!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
