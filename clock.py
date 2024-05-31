from datetime import datetime, timezone

print("hallo")

while True:
    print(f"\033[F{datetime.now(timezone.utc).isoformat(timespec='seconds')}")
    # print(f"\033[F{datetime.now(timezone.utc).strftime('%c')}")
