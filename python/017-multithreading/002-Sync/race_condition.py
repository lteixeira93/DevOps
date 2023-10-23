import threading
import random
import time

from typing import List

class Account:
  def __init__(self, amount = 0) -> None:
    self.amount = amount
        
def main():
  # Creating accounts
  accounts = create_accounts()
  
  # Sum of accounts amount
  total = sum(account.amount for account in accounts)
  print("Initializing tranfers")
  
  # Threads are using same funtion and resources, creating a race condition
  tasks = [
    threading.Thread(target=services, args=(accounts, total)),
    threading.Thread(target=services, args=(accounts, total)),
    threading.Thread(target=services, args=(accounts, total)),
    threading.Thread(target=services, args=(accounts, total)),
    threading.Thread(target=services, args=(accounts, total)),
    threading.Thread(target=services, args=(accounts, total))
  ]
  
  [ task.start() for task in tasks ]
  [ task.join() for task in tasks ]
  
  print("Tranfers completed")
  
  validate_bank(accounts, total)
  
def services(accounts: List[Account], total: int) -> None:
  for _ in range(1, 10_000):
    c1, c2 = take_two_accounts(accounts)
    value = random.randint(1, 100)
    transfer(c1, c2, value)
    validate_bank(accounts, total)
    
def create_accounts() -> List[Account]:
  return [
    Account(amount=random.randint(5_000, 10_000)),
    Account(amount=random.randint(5_000, 10_000)),
    Account(amount=random.randint(5_000, 10_000)),
    Account(amount=random.randint(5_000, 10_000)),
    Account(amount=random.randint(5_000, 10_000)),
    Account(amount=random.randint(5_000, 10_000)),
  ]
  
def transfer(source: Account, destiny: Account, value: int) -> None:
  if source.amount < value:
    # Not enough balance
    return

  source.amount -= value
  time.sleep(0.001)
  destiny.amount += value
  
def validate_bank(accounts: List[Account], total: int):
  current = sum(account.amount for account in accounts)
  
  if current != total:
    print(f"Error: Inconsistent balance. EUR {current:.2f} vs {total:.2f}", flush=True)
  else:
    print(f"Done: Consistent balance. EUR {total:.2f}", flush=True)
    
def take_two_accounts(accounts: List[Account]):
  c1 = random.choice(accounts)
  c2 = random.choice(accounts)
  
  while c1 == c2:
    c2 = random.choice(accounts)
    
  return c1, c2

if __name__ == "__main__":
  main()