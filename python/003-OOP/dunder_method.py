class Book():
    def __init__(self, title, author, pages):
        self.title  = title
        self.author = author
        self.pages  = pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("Book deleted")
    
def main():    
    b = Book("Python", "Joseph", 300)
    print(b) # print tries to print __str__ method which is now overloaded by the class
    print(str(b))
    print(len(b))
    del(b)
# end def

if __name__ == "__main__":
    main()