from datetime import datetime, timedelta
from subprocess import DEVNULL, Popen
from sys import argv
from time import sleep

ct = datetime.fromisoformat(argv[1])
# delay = timedelta(seconds=6, milliseconds=250)
delay = timedelta(seconds=29, milliseconds=250)
pip_start = ct - delay

if datetime.now(tz=pip_start.tzinfo) > pip_start:
    print("whoops missed it")
    exit()

print()

while datetime.now(tz=pip_start.tzinfo) < pip_start:
    diff = ct - datetime.now(tz=ct.tzinfo).replace(microsecond=0)
    print("\033[F" + str(diff))

Popen(["mpv", "bbc-2018.flac"], stdout=DEVNULL, stderr=DEVNULL)

while datetime.now(tz=ct.tzinfo) < ct:
    diff = ct - datetime.now(tz=ct.tzinfo)
    print("\033[F" + str(diff)[0:-5])

print("Hooray!")
sleep(1)
