class Release:
    r_amount = 0
    def __init__(self, name):
        Release.r_amount = Release.r_amount + 1
        self.release_number = Release.r_amount
        self.name = name
    def print_info(self):
        print(f"{self.release_number}. Release: {self.name}")

class Book(Release):

    def __init__(self, name, author, pageamount):
        self.author = author
        self.pageamount = pageamount
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"Author of the book: {self.author}. ")
        print(f"The pageamount of the book: {self.pageamount}.")

class Magazine(Release):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)
    def print_info(self):
        super().print_info()
        print(f"The chief editor of the magazine: {self.chief_editor}. ")

publish = []
publish.append(Book("Hytti n:o 6", "Rosa Liksom", 200))
publish.append(Magazine("Aku Ankka", "Aki hyppääjä"))

for t in publish:
    t.print_info()