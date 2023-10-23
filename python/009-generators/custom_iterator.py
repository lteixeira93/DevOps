class Counter:
    def __init__(self, smallest, biggest):
        self.smallest = smallest
        self.biggest = biggest
     
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.smallest < self.biggest:
            number = self.smallest
            self.smallest = self.smallest + 1
            return number
        raise StopIteration
       
con = Counter(1, 6)
it = iter(con)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


for n in Counter(1, 61):
    print(n)