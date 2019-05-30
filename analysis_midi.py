import time


def delay():
    print("delay")
    time.sleep(1)

t = time.time()
print("detect input__")
print(int(round(t * 1000)))
delay()
t = time.time()

print(int(round(t * 1000)))
