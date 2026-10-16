import os

from flask import Flask

COUNTER_FILE = os.getenv("COUNTER_FILE", "/usr/src/app/files/pingpong.txt")

app = Flask(__name__)

counter = 0


def save_counter() -> None:
    os.makedirs(os.path.dirname(COUNTER_FILE), exist_ok=True)
    with open(COUNTER_FILE, "w") as f:
        f.write(str(counter))


@app.route("/pingpong")
def pingpong():
    global counter
    response = f"pong {counter}"
    counter += 1
    save_counter()
    return response


if __name__ == "__main__":
    port = int(os.getenv("PORT", 3000))
    print(f"Server started in port {port}", flush=True)
    app.run(host="0.0.0.0", port=port)
