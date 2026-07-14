class Book:

    def __init__(self, title, author, is_borrowed):

        self.title = title

        self.author = author

        self.is_borrowed = is_borrowed

    def borrow(self):

        self.is_borrowed = True

        print(self.is_borrowed)

    def return_book(self):

        self.is_borrowed = False

        print(self.is_borrowed)

story = Book("Story Book", "Joyce", True)
story.borrow()
story.return_book()

fantasy = Book("Fantasy Book", "Joyce", True)

fantasy.borrow()

fantasy.return_book()

Adventure = Book("Aventure Book", "Joyce", True)

Adventure.borrow()

Adventure.return_book(