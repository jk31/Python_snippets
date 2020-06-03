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
  


