import os

from flask import Flask, Response

FILE_PATH = os.getenv("FILE_PATH", "/usr/src/app/files/log.txt")
COUNTER_FILE = os.getenv("COUNTER_FILE", "/usr/src/app/files/pingpong.txt")

app = Flask(__name__)


def read_file(path: str, default: str) -> str:
    try:
        with open(path) as f:
            return f.read().strip()
    except FileNotFoundError:
        return default


@app.route("/")
def index():
    line = read_file(FILE_PATH, "No log lines yet")
    pongs = read_file(COUNTER_FILE, "0")
    return Response(f"{line}.\nPing / Pongs: {pongs}\n", mimetype="text/plain")


if __name__ == "__main__":
    port = int(os.getenv("PORT", 3000))
    print(f"Server started in port {port}", flush=True)
    app.run(host="0.0.0.0", port=port)
