import threading
import time


def teste(name: str = ""):
    print(f"ran {name}!")
    time.sleep(1)
    print(f"done {name}!!")
    time.sleep(0.85)
    print(f"Really done {name}!!!")


x = threading.Thread(target=teste, args=("João",))
x.start()
print(threading.activeCount())
time.sleep(1.2)
print("finnaly")
