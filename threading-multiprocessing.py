
######## THREADING

import threading
import time

start = time.perf_counter()

def do_something(seconds):
  print("sleep ")
  time.sleep(seconds)
  return f"Done {seconds}"
 
t1 = threading.Thread(target=do_something, args=[2])
t2 = threading.Thread(target=do_something, args=[2])

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(round(finish-start, 2))

##### more with loops

threads = []
for _ in range(10):
  t = threading.Tread(target=do_something, args=[2])
  t.start()
  threads.append(t)

for thread in threads:
  thread.join()
  
####
  
import concurrent.futures

with concurrent.futures.ThreadPoolExecutor() as executor:
  f1 = executor.submit(do_something, 2)
  print(f1.result())

####

with concurrent.futures.ThreadPoolExecutor() as executor:
  secs = [5, 4, 3, 2, 1]
  results = [executor.submit(do_something, sec) for sec in secs]
  
  for f in concurrent.futures.as_completed(results): # in order that they are completed
    print(f.results())
    
###

with concurrent.futures.ThreadPoolExecutor() as executor:
  executor.map(download_function, urls)
  
########## MULTIPROCESSING

import time
import multiprocessing

start = time.perf_counter()

def do_something(seconds=2):
  print("sleep ")
  time.sleep(seconds)
  return f"Done {seconds}"

p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

p1.start()
p2.start()

p1.join()
p2.join()

####

processes = []
for _ in range(10):
  p = multiprocessing.Process(target=do_something, args=[3])
  p.start()
  processes.append(p)
  
for process in processes:
  process.join()

finish = time.perf_counter()


###

import concurrent.futures

with concurrent.futures.ProcessPoolExecutor() as executor:
  results = [executor.submit(do_something, 1) for _ in range(10)]
  
  for f in concurrent.futures.as_completed(results):
    print(f.result())
    
    
secs = [5, 4, 3, 2, 1]
results = executor.map(do_something, secs)
