import os

from flask import Flask, Response

FILE_PATH = os.getenv("FILE_PATH", "/usr/src/app/files/log.txt")

app = Flask(__name__)


@app.route("/")
def index():
    try:
        with open(FILE_PATH) as f:
            content = f.read()
    except FileNotFoundError:
        content = "No log lines yet\n"
    return Response(content, mimetype="text/plain")


if __name__ == "__main__":
    port = int(os.getenv("PORT", 3000))
    print(f"Server started in port {port}", flush=True)
    app.run(host="0.0.0.0", port=port)
