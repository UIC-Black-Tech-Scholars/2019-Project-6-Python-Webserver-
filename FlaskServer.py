from flask import Flask
from flask import render_template, send_file, jsonify, request
import json

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == "GET":
        return "Hello World!"
    else:
        print(request.form)
        print(request.data)
        recieved_data = json.loads(
            (request.form if request.form else request.data)
                .decode("utf-8")
        )
        print(recieved_data)
        return jsonify({
            "Hello": "World!",
            "Recieved": recieved_data
        })


if __name__ == "__main__":
    host = "localhost"
    # host = "0.0.0.0"
    port = 8080
    print(f"Starting the webserver on {host}:{port}")

    app.run(host=host, port=port)
