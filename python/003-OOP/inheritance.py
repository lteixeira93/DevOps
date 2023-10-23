# All classes inherits from object if not inherits from another class - isinstance(class, object) -> True
# class Animal(object): Behind the scenes
# Overriding is the best exemplification of polimorphism
class Animal():
    
    def __init__(self):
        print("Animal Created")
    
    def who_am_i(self):
        print("Animal")
    
    def eat(self):
        print("Eating")
        
    def bark(self):
        raise NotImplementedError("Subclass must implement pure virtual method")
        
class Coyote(Animal):   
    
    def __init__(self):
        # super().__init__("Animal")
        super("Animal")
        Animal.__init__(self)
        print("Wolf created")
    
    def eat(self):
        print("Coyote Eating")
        
    def noising(self):
        print("Coyote noising")
        
class Wolf(Animal):   
    
    def __init__(self):
        Animal.__init__(self)
        print("Wolf created")
    
    def eat(self):
        print("Wolf Eating")
        
    def auu(self):
        print("Wolf Auuing")
        
class Dog(Coyote, Wolf):   
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
        
def main():    
    my_dog = Coyote()
    my_dog.eat()
    # my_dog.bark() -> Must implement pure virtual method
    
    # print(help(Dog))
    
    # print(Animal.who_am_i.__annotations__) # Verify funtion in depth
# end def

if __name__ == "__main__":
    main()