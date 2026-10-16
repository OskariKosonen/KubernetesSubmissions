import os

from flask import Flask

app = Flask(__name__)

counter = 0


@app.route("/pingpong")
def pingpong():
    global counter
    response = f"pong {counter}"
    counter += 1
    return response


if __name__ == "__main__":
    port = int(os.getenv("PORT", 3000))
    print(f"Server started in port {port}", flush=True)
    app.run(host="0.0.0.0", port=port)
