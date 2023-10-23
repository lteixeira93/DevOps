class Dog():
    species = 'mammal'
    
    def __init__(self, breed):
        self.breed = breed
    
    def bark(self):
        print("Bark of {}".format(self.breed))
    
def main():    
    my_dog = Dog(breed="German Shephard")
    print(my_dog.breed)
    my_dog.bark()
# end def

if __name__ == "__main__":
    main()