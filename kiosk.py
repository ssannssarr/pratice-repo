# LIBRARY      
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
        "Author":"Chetan Bhagat",
        "Stock": 15,
    },
    "Atomic Habit": {
        "name":"Atomic Habit",
        "Availability": True,
        "price":60.75,
        "Author":"James Clear",
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


# TEXT SECTION
HELP_TEXT = """
  Available Commands:
 +---------------------------------------------------------+
 | /list -a    - List all available books in the library   |
 | /list -un   - List all unavailable books in the library |
 | /list -f    - List all books                            |
 | /srch       - Search for a book in the library          |
 | /buy        - Buy a book from the library               |
 | /exit       - Exit the library                          |
 | /help       - Show this help message                    |
 +---------------------------------------------------------+
"""
WELCOME_TEXT = """
Welcome to SannS library!!^_^
We have a wide range of books for you to choose from.        
For any query email us @sannslib@gmail.com
Type "/help" to see the available commands
"""
BYE_TEXT = "Goodbye!!\nHave a good day!"

# The Info Func
def info(book_name):
    for book in library_books:
        if book.lower() == book_name:
            return f"""
 NAME           : {library_books.get(book).get("name")}        
 AVAILABILITY   : {library_books.get(book).get("Availability")}
 PRICE          : {library_books.get(book).get("price")}$    
 AUTHOR         : {library_books.get(book).get("Author")}      
 STOCK          : {library_books.get(book).get("Stock")}                
"""
     
# Searching Function
def srch():
     print("\nEnter the book Name you want to query:")
     book_name = input("[search]>>").strip().lower()
     print(info(book_name))

# List All Available Books
def list_a():
     print("\nThese Are The Available Books In Our Library:")
     for book in library_books:
        if library_books[book].get("Availability"):
            print("  *",book)
     
# List All Unvailable currently
def list_un():
    print("\nThese Books Are Currently Unvailable In Our Library:")
    for book in library_books:
        if library_books[book].get("Availability") == False:
            print("  *",book)

# List Full Library:
def list_f():
    print("These are all books some are currently not available*")
    for book in library_books:
        if library_books.get(book).get("Availability"):
            print(" -",book)
        else:
            print(" -",book+"*")
        
def prebook(book,buy_book):
    print(f"""
The book {book} is currently unavailable
If you want you can pre-book it
For book details use "/info"
""")
    unavai = input("[pre-book]>>").strip().lower()
    if unavai == "/info":
        print(info(buy_book))
        print("Will you Pre-Book:(y/n)")
        prbk = input("[pre-book]>>").strip().lower()
        if prbk == "y":
            print("We will inform the sec the book appears to us. (^-^)")
        else:
            print("Your wish!!")
    else:
        print("You can see our other books by cmd ='/list' ")   

# Buy function 
def buy():
    print(f"\nWhich book will you buy?")
    found = False
    buy_book = input("[buy]>> ").strip().lower()
    for book in library_books:
        if book.lower() == buy_book:
            found = True

            if library_books.get(book).get("Availability"):
                print(f"""
The book {book} is available. The info is listed below. {info(buy_book)}
Will You Buy?(y/n)""" )
                buy = input("[buy]>> ").strip().lower()
                if buy == "y":
                    library_books[book]["Stock"] -= 1
                    print(f"""
The book {book} of price {library_books.get(book).get("price")}$ is out for delivery.^_^
HAPPY READING
For any query email us @sannslib@gmail.com""")
                    break
                else:
                    print("Whenever you change your mind let us know - SannS Library ")
            elif library_books.get(book).get("Availability") == False:
                prebook(book,buy_book)

    if not found:
            print(f"The Book {buy_book} isnt available in our library.(T.T)")




# Main Process 
print(WELCOME_TEXT)
user_input = ""
try:
    while user_input != "/exit":
        user_input = input(">>").strip().lower()
        if user_input == "/list -a":
            list_a()
        elif user_input == "/list -f":
            list_f()
        elif user_input == "/list -un":
            list_un()
        elif user_input == "/srch":
            srch()
        elif user_input == "/help":
            print(HELP_TEXT)
        elif user_input == "/buy":
            buy()
        elif user_input != "/exit":
             print("\nThe command you typed didnt support.T_T")
    print(BYE_TEXT)
except KeyboardInterrupt:
     print("\n"+BYE_TEXT)
