from flask import Flask, abort

app = Flask(__name__)

@app.route("/")
def two_hundred():
    return "<h1>200! all is good from SKD</h1>"

@app.route("/error")
def error():
    abort(500, "oops, some error")

if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")