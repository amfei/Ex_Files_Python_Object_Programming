# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPEs=("Paperback", "Hardcover", "Pdf")
    # TODO: double-underscore properties are hidden from other classes

    # TODO: create a class method
    @classmethod
    def getbooktype(cls):
        return cls.BOOK_TYPEs

    # TODO: create a static method

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype  in Book.BOOK_TYPEs):
            raise ValueError(f"{booktype} is not valid book type")
        else:
            self.booktype=booktype 


# TODO: access the class attribute
print(Book.getbooktype())

# TODO: Create some book instances
b1 = Book("Title 1", "Paperback")
b2 = Book("Title 2","Pdf")

# TODO: Use the static method to access a singleton object
