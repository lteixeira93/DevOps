class Animal():
    # Abstract class: Never instantiated
    def __init__(self, name):
        self.name = name
     
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method") # Pure virtual

class Dog(Animal):   
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return self.name + " Woof"

class Cat():   
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return self.name + " Meow"
    
def main():    
    niko = Dog("Niko")
    felix = Cat("Felix")
    animal = Animal("Fred")
    # animal.speak()
    
    print(niko.speak())
    print(felix.speak())

# end def

if __name__ == "__main__":
    main()
    
'''
Example:
Class to open a file.
The class shall be abstract and provide the method Open()
So the derived class implements different types of open (xlsx, json, etc)
'''