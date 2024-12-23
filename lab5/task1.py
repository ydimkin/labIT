class Book:

    def __init__(self, title: str, author: str, year: int):
        
        self.__title = title
        self.__author = author
        self.__year = year

    
    def get_info(self):
        return f"Название книги: {self.__title}, Автор: {self.__author}, Год издания: {self.__year}"



book = Book("Какое-то название", "автор", 2024)

print(book.get_info())
