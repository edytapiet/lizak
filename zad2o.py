class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library: {self.city}, {self.street}, {self.zip_code}, open: {self.open_hours}, tel: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Employee: {self.first_name}, {self.last_name}, hired: {self.hire_date}, " 
                f"born: {self.birth_date}, adress: {self.city}, {self.street}, {self.zip_code},"
                f"tel: {self.phone}")


class Student:
    def __init__(self, first_name, last_name, city):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city

    def __str__(self):
        return f"Student: {self.first_name}, {self.last_name}, city: {self.city}"




class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Book by {self.author_name}, {self.author_surname}, ({self.publication_date},"
                 f"{self.number_of_pages} pages) {self.library}")



class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
         book_list = "\n".join([str(book) for book in  self.books])
         return (f"Order date: {self.order_date}\n"
                 f"Employee: {self.employee}\n"
                 f"Student: {self.student}\n"
                 f"Book:\n  {book_list}")



lib1 = Library('Kraków', 'Floriańska 12', '31-001', '10:00 - 18:00', '444-333-567')
lib2 = Library('Warszawa', 'Krakowskie Przedmiescie 1', '00-002', '9:00-17:00', '123-546-987')


book1 = Book(lib1, 1945, 'George', 'Orwell', 120 )
book2 = Book(lib1, 2018, 'James', 'Clear', 320)
book3 = Book(lib2, 1915, 'Franz', 'Kafka', 100)
book4 = Book(lib2, 1988, 'Paulo', 'Coelho', 200)
book5 = Book(lib2, 1925, 'Franz', 'Kafka', 250)

emp1 = Employee('Karol', 'Poleski', '2019-03-29', '1998-06-11', 'Kraków', 'Floriańska 12', '00-003', '987-645-754')
emp2 = Employee("Jan", "Nowak", "2020-02-20", "1985-07-03", "Kraków", "Rynek 15", "31-002", "123-456-789")
emp3 = Employee("Ewa", "Wiśniewska", "2015-11-30", "1988-03-21", "Warszawa", "Szeroka 5", "00-003", "565-564-943")

stu1 = Student("Ola", "Zając", "Warszawa")
stu2 = Student("Marek", "Lis", "Kraków")
stu3 = Student("Karolina", "Dąbrowska", "Gdańsk")

order1 = Order(emp1, stu1, [book1, book3], "2024-10-10")
order2 = Order(emp3, stu3, [book2, book4, book5], "2024-11-15")

print(order1)
print("-" * 20)
print(order2)
