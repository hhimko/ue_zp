from zad1 import Student


class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return f"Library(city={self.city}, street={self.street}, zip_code={self.zip_code}, open_hours={self.open_hours}, phone={self.phone})"

class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str, city: str, street: str, zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return f"Employee(first_name={self.first_name}, last_name={self.last_name}, hire_date={self.hire_date}, birth_date={self.birth_date}, city={self.city}, street={self.street}, zip_code={self.zip_code}, phone={self.phone})"

class Book:
    def __init__(self, library: Library, publication_date: str, author_name: str, author_surname: str, number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f"Book(library={str(self.library)}, publication_date={self.publication_date}, author_name={self.author_name}, author_surname={self.author_surname}, number_of_pages={self.number_of_pages})"


class Order:
    def __init__(self, employee: Employee, student: Student, books: list[Book], order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        books = f"[{', '.join(str(b) for b in self.books)}]" 
        return f"Order(employee={str(self.employee)}, student={self.student}, books={books}, order_date={self.order_date})"


if __name__ == "__main__":
    l1 = Library("Katowice", "Bogucicka", "40-215", "8:00 - 16:00", "+48 012 345 678")
    l2 = Library("Rybnik", "Gliwicka", "44-220", "7:00 - 14:00", "+48 987 654 321")

    b1 = Book(l1, "01.01.2003", "Dawid", "Cyganek", 420)
    b2 = Book(l1, "08.12.2020", "Kamil", "Glac", 1264)
    b3 = Book(l2, "11.07.2016", "Kacper", "Hałaczkiewicz", 178)
    b4 = Book(l2, "04.04.2008", "Julia", "Caputa", 68)
    b5 = Book(l2, "25.06.2011", "Krzysztof", "Górny", 239)

    e1 = Employee("Bartosz", "Dziewit", "17.07.2018", "14.01.1986", "Sosnowiec", "Katowicka", "41-180", "+48 111 222 333")
    e2 = Employee("Adam", "Małysz", "10.11.2002", "18.11.1972", "Szczecin", "Poznanska", "54-318", "+48 123 649 832")
    e3 = Employee("Jan", "Paweł", "08.02.2024", "14.01.1920", "Wadowice", "Szeroka", "24-070", "+48 900 601 320")

    s1 = Student("Agata Kudla", [10, 20, 80, 100, 95.5])
    s2 = Student("Sebastian Matuszczyk", [60, 30.5, 20, 100, 65.5])
    s3 = Student("Karol Cyganek", [0, 0, 0, 10, 35])

    o1 = Order(e2, s1, [b2, b1], "15.12.2024")
    o2 = Order(e1, s2, [b5, b3, b4], "11.10.2024")

    print(o1)
    print(o2)
    