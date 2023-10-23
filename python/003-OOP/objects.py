class Client:
    def __init__(self, name, id):
        self.__name = name
        self.__id   = id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def id(self):
        return self.__id
    
    def say(self):
        print(f"Client {self.__name} says: Hi")
        
class Account:
    counter = 4999
    
    def __init__(self, limit, amount, client):
        self.__number   = Account.counter + 1
        self.__limit    = limit
        self.__amount   = amount
        self.__client   = client
        Account.counter = self.__number
        
    @property # getter
    def limit(self):
        return self.__limit
    
    @limit.setter # setter
    def limit(self, new_limit):
        self.__limit = new_limit
        
    def show_client(self):
        print(f"Client name is: {self.__client._Client__name}")
        
client_1 = Client("John Marston", "123.456.789-00")
cc = Account(1000, 2000, client_1)

cc.show_client()

print(dir(cc)) # Shows how to access private method and attributes (Name Mangling)
cc._Account__client.say() # Wrong way to access private, use @property instead

# cc.__client.say() -> Error

print(cc.limit)
cc.limit = 40000
print(cc.limit)

print(cc.__dict__)
