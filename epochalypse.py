from datetime import datetime

print()
while True:
    print(f"\033[F{datetime.now().timestamp() / 2 ** 31}")
