import os
import threading
import time
import uuid
from datetime import datetime, timezone

from flask import Flask

RANDOM_STRING = str(uuid.uuid4())

app = Flask(__name__)


def timestamp() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def status() -> str:
    return f"{timestamp()}: {RANDOM_STRING}"


def log_loop() -> None:
    while True:
        print(status(), flush=True)
        time.sleep(5)


@app.route("/")
def index():
    return status()


if __name__ == "__main__":
    port = int(os.getenv("PORT", 3000))
    threading.Thread(target=log_loop, daemon=True).start()
    print(f"Server started in port {port}", flush=True)
    app.run(host="0.0.0.0", port=port)
