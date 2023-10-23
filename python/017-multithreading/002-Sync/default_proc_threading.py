
# mkvirtualenv default_proc -p python3
import datetime
import math
import threading
import multiprocessing

def main():
  num_cores = multiprocessing.cpu_count()
  print(f"Initializing with {num_cores} cores.")
  
  initial = datetime.datetime.now()
  
  threads = []
  
  for n in range(1, num_cores + 1):
    ini = 50_000_000 * (n - 1) / num_cores  
    end = 50_000_000 * (n) / num_cores 
    
    print(f"Core {n} processing from {ini} to {end}")
    
    threads.append(
      threading.Thread(
        target=compute,
        kwargs={'initial': ini, "end": end},
        daemon=True
      )
    )
  
  [th.start() for th in threads]
  [th.join() for th in threads]  
  
  time_val = datetime.datetime.now() - initial
  
  print(f"Finished in {time_val.total_seconds():.2f} seconds.")
  
def compute(end, initial = 1):
  # Function to waste time
  pos = initial
  factor = 1000*1000
  
  while pos < end:
    pos += 1
    math.sqrt((pos - factor)*(pos - factor))
    
if __name__ == "__main__":
  main()
  # Finished in 8.22 seconds
  