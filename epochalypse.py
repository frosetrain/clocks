from datetime import datetime

print()
print()
while True:
    print(f"\033[F\033[F{datetime.now().timestamp() / 2 ** 31}")
    print(datetime.fromtimestamp(2 ** 31 * 0.8) - datetime.now())
