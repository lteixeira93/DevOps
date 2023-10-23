
# mkvirtualenv default_proc -p python3
import threading
import time

def main():
  th = threading.Thread(target=count, args=('elefante', 10))
  th.start() # Add thread in 'ready to execute' pool
  
  print("Running in parallel while thread is executing...")
  print('Geek '*2)
  
  th.join()
  
  print('Done')
  
def count(wht, num):
  for n in range(1, num + 1):
    print(f"{n} {wht}(s)...")
    time.sleep(10)
    
if __name__ == "__main__":
  main()
  # Finished in 13.18 seconds
  