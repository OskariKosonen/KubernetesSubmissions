import time
import uuid
from datetime import datetime, timezone

RANDOM_STRING = str(uuid.uuid4())


def timestamp() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


if __name__ == "__main__":
    while True:
        print(f"{timestamp()}: {RANDOM_STRING}", flush=True)
        time.sleep(5)
