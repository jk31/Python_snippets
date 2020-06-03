import threading
import time

start = time.perf_counter()

def do_something():


finish = time.perf_counter()

print(round(finish-start, 2))
