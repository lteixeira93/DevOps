import collections

Person = collections.namedtuple("Person", "father, kids")

john = Person("John", ["Sally", "Joe"])
print(john)

john.kids.append("Claire")

print(john)
