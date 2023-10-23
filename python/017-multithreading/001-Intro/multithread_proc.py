
# mkvirtualenv default_proc -p python3
import threading
import time

def count(wht, num):
  for n in range(1, num + 1):
    print(f"{n} {wht}(s)...")
    time.sleep(2)
    
def main():
  threads = [
    threading.Thread(target=count, args=('elefante', 14)),
    threading.Thread(target=count, args=('buraco', 8)),
    threading.Thread(target=count, args=('dinheiro', 32)),
    threading.Thread(target=count, args=('pato', 20))
  ]
  
  [ th.start() for th in threads ]  # Add thread in 'ready to execute' pool
  
  print("Running in parallel while thread is executing...")
  print('Geek '*1)
  
  [ th.join() for th in threads ]
  
  print('Done')
  
if __name__ == "__main__":
  main()
  # Finished in 13.18 seconds
  