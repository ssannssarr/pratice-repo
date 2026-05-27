

library_books = {
    "It Ends With Us":{
        "name":"It Ends With Us",
        "Availability": True,
        "price":99.5,
        "Author":"Collen Hoover",
        "Stock": 15,
    },
    "1984":{
        "name":"1984",
        "Availability": False,
        "price":80.50,
        "Author":"Collen Hoover",
        "Stock": 0,
    },
    "One Indian Girl": {
        "name":"One Indian Girl",
        "Availability": True,
        "price":99.5,
        "Author":"Collen Hoover",
        "Stock": 15,
    },
    "Atomic Habit": {
        "name":"Atomic Habit",
        "Availability": True,
        "price":60.75,
        "Author":" James Clear",
        "Stock": 15,
    },
    "The Alchemist": {
        "name":"The Alchemist",
        "Availability": False,
        "price":99.5,
        "Author":"Paulo Coelho",
        "Stock": 0,
    },
    "The Subtle Art of Not Giving a F*ck": {
        "name":"The Subtle Art of Not Giving a F*ck",
        "Availability": False,
        "price":70.00,
        "Author":"Mark Manson",
        "Stock": 0,
    },
    "The Power of Now": {
        "name":"The Power of Now",
        "Availability": True,
        "price":100.00,
        "Author":"Eckhart Tolle",
        "Stock": 15,
    },
    "The 5 AM Club": {
        "name":"The 5 AM Club",
        "Availability": False,
        "price":500.00,
        "Author":"Robin Sharma",
        "Stock": 0,
    },
    "The Great Gatsby": {
        "name":"The Great Gatsby",
        "Availability": True,
        "price":85.00,
        "Author":"F. Scott Fitzgerald",
        "Stock": 15,
    },
}

def info(book_name):
    for book in library_books:
        if book.lower() == book_name:
            return f"""
NAME : {library_books.get(book).get("name")}
AVAILABILITY : {library_books.get(book).get("Availability")}
PRICE : {library_books.get(book).get("price")}$
AUTHOR : {library_books.get(book).get("Author")}
STOCK : {library_books.get(book).get("Stock")}

"""

usr_in = input(">>").strip().lower()
if usr_in == "/srch":
    print("\nEnter the book Name you want to query:")
    book_name = input("[search]>>").strip().lower()
    print(info(book_name))
    