import os
import time
import uuid
from datetime import datetime, timezone

RANDOM_STRING = str(uuid.uuid4())
FILE_PATH = os.getenv("FILE_PATH", "/usr/src/app/files/log.txt")


def timestamp() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def status() -> str:
    return f"{timestamp()}: {RANDOM_STRING}"


def log_loop() -> None:
    while True:
        line = status()
        with open(FILE_PATH, "a") as f:
            f.write(line + "\n")
        print(line, flush=True)
        time.sleep(5)


if __name__ == "__main__":
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
    print(f"Writing to {FILE_PATH}", flush=True)
    log_loop()
