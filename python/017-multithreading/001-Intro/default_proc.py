
# mkvirtualenv default_proc -p python3
import datetime
import math

def main():
  initial = datetime.datetime.now()
  
  compute(end=50_000_000)
  
  time_val = datetime.datetime.now() - initial
  
  print(f"Finished in {time_val.total_seconds():.2f} seconds")
  
def compute(end, initial = 1):
  # Function to waste time
  pos = initial
  factor = 1000*1000
  
  while pos < end:
    pos += 1
    math.sqrt((pos - factor)*(pos - factor))
    
if __name__ == "__main__":
  main()
  # Finished in 13.18 seconds
  