from typing import Generator

# Thread uses Generator as it can be stopped and get the next value retrieved (Static)
def fibo() -> Generator[int, None, None]:
    val: int = 0
    next_val: int = 1
    
    while True:
        val, next_val = next_val, val + next_val
        yield val
        
for n in fibo(): # for calls next() implicitly
    print(n, end=', ')
    if n > 100:
        break
    
print("\nDone")