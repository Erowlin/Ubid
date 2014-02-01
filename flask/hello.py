from flask import Flask
app = Flask(__name__)

app.debug = True

@app.route("/<username>")
def hello(username):
    return "Hello, %s" % username
if __name__ == "__main__":
    app.run()
