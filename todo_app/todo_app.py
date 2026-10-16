import os
import threading
import time
import urllib.request

from flask import Flask, render_template, send_file

FILE_DIR = os.getenv("FILE_DIR", "/usr/src/app/files")
IMAGE_URL = os.getenv("IMAGE_URL", "https://picsum.photos/1200")
IMAGE_MAX_AGE_SECONDS = int(os.getenv("IMAGE_MAX_AGE_SECONDS", 600))

IMAGE_PATH = os.path.join(FILE_DIR, "image.jpg")
# Exists when the expired image has already been served its one extra time
EXPIRED_MARKER = os.path.join(FILE_DIR, "expired_served")

MAX_TODO_LENGTH = 140
TODOS = ["Learn JavaScript", "Learn React", "Build a project"]

app = Flask(__name__)
image_lock = threading.Lock()


def download_image() -> None:
    tmp_path = IMAGE_PATH + ".tmp"
    with urllib.request.urlopen(IMAGE_URL, timeout=10) as response, open(tmp_path, "wb") as f:
        f.write(response.read())
    os.replace(tmp_path, IMAGE_PATH)
    if os.path.exists(EXPIRED_MARKER):
        os.remove(EXPIRED_MARKER)
    print(f"Downloaded new image from {IMAGE_URL}", flush=True)


def ensure_image() -> None:
    with image_lock:
        if not os.path.exists(IMAGE_PATH):
            download_image()
            return
        age = time.time() - os.path.getmtime(IMAGE_PATH)
        if age < IMAGE_MAX_AGE_SECONDS:
            return
        if not os.path.exists(EXPIRED_MARKER):
            open(EXPIRED_MARKER, "w").close()
            return
        try:
            download_image()
        except OSError as e:
            print(f"Image download failed, keeping old image: {e}", flush=True)


@app.route("/")
def index():
    ensure_image()
    version = int(os.path.getmtime(IMAGE_PATH))
    return render_template("index.html", version=version, todos=TODOS, max_length=MAX_TODO_LENGTH)


@app.route("/image")
def image():
    return send_file(IMAGE_PATH, mimetype="image/jpeg")


@app.route("/shutdown")
def shutdown():
    # For testing that the cached image survives a container crash
    print("Shutting down", flush=True)
    os._exit(1)


if __name__ == "__main__":
    os.makedirs(FILE_DIR, exist_ok=True)
    port = int(os.getenv("PORT", 3000))
    print(f"Server started in port {port}", flush=True)
    app.run(host="0.0.0.0", port=port)
