# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, price, page):
        self.title = title
        # TODO: add properties
        self.author = author
        self.price = price
        self.page = page
        
        self.__secret="This is a secret attribute"

    # TODO: create instance methods
    def getPrice(self):
        if hasattr(self,"_discount"):
            return self.price-(self.price * self._discount)
        else:
            return self.price
            
    def setDiscout(self,amount):
        self._discount=amount
            
            
            


# TODO: create some book instances
b1 = Book("War and Peace", "amir", 50,1458)
b2 = Book("The Catcher in the Rye", "ehsan",55,1444)

# # TODO: print the price of book1
# print(f"price of Book 1 is {b1.getPrice()}")
# print(f"price of Book 2 Befor discount is  {b2.getPrice()}")

# # TODO: try setting the discount
# b2.setDiscout(0.25)
# print(f"price of Book 2 After discount is  {b2.getPrice()}")


# TODO: properties with double underscores are hidden by the interpreter
print(b2._Book__secret)