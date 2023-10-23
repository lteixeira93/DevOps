# Inter Threads Communication
'''Queue is thread safe for thread communication'''
import time
import colorama

from threading import Thread
from queue import Queue

def producer(queue):
    for i in range(1, 11):
      print(colorama.Fore.GREEN + f"Data {i} generated", flush=True)
      time.sleep(2)
      queue.put(i)

def consumer(queue):
  while queue.qsize() > 0:
    val = queue.get()
    print(colorama.Fore.RED + f"Data {val * 2} processed", flush=True)
    time.sleep(1)
    queue.task_done()
    
if __name__ == "__main__":
  print(colorama.Fore.WHITE + "System Initialized", flush=True)
  queue = Queue()
  
  th1 = Thread(target=producer, args=(queue,))
  th2 = Thread(target=consumer, args=(queue,))
  
  th1.start()
  th1.join()
  
  th2.start()
  th2.join()
  