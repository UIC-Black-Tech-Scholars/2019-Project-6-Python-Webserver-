from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/hello")
@app.route("/hello/<string:name>")
def hello_page(name=None):
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    host = "localhost"
    # host = "0.0.0.0"
    port = 8080
    print(f"Starting the webserver on {host}:{port}")

    app.run(host=host, port=port)
