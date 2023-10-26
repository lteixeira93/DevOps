from collections import deque

deq = deque("ee")

deq.append('k')
deq.appendleft('G')
print(deq)

deq.pop()
deq.popleft()
print(deq)