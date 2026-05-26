import pandas as pd

# LIBRARY      
library_books = {
    "It Ends With Us":{
        "Availability": True,
        "prize":99.5,
        "Author":"Collen Hoover"
    },
    "1984":{
        "Availability": False,
        "prize":80.50,
        "Author":"Collen Hoover"
    },
    "One Indian Girl": {
        "Availability": True,
        "prize":99.5,
        "Author":"Collen Hoover"
    },
    "Atomic Habit": {
        "Availability": True,
        "prize":60.75,
        "Author":" James Clear"
    },
    "The Alchemist": {
        "Availability": False,
        "prize":99.5,
        "Author":"Paulo Coelho"
    },
    "The Subtle Art of Not Giving a F*ck": {
        "Availability": True,
        "prize":70.00,
        "Author":"Mark Manson"
    },
    "The Power of Now": {
        "Availability": True,
        "prize":100.00,
        "Author":"Eckhart Tolle"
    },
    "The 5 AM Club": {
        "Availability": False,
        "prize":500.00,
        "Author":"Robin Sharma"
    },
    "The Great Gatsby": {
        "Availability": True,
        "prize":85.00,
        "Author":"F. Scott Fitzgerald"
    },
}


# TEXT SECTION
HELP_TEXT = """
 type "/list" to list all available books in our library 
 type "/search" to search a specific book info
 type "/exit" to exit our library
 type "/help" to open this menu
"""
WELCOME_TEXT = """
 Welcome to SannS library!!^_^
 type "/list" to list all available books in our library 
 type "/search" to search a specific book info
 type "/exit" to exit our library
 type "/help" to open command menu
 Have good reading!! yay          
"""
BYE_TEXT = "Goodbye!!\n Have a good day!"



# Searching Function
def srch():
     book_name = input("Enter Book Name:")
     if book_name in library_books:
        print(pd.Series(library_books.get(book_name)))
     else:
        print(f"The book {book_name} is not available in our library \nTo see the the available books use Cmd:'/list'")       
# List All Available Books
def list_books():
    for book in library_books:
        if library_books[book].get("Availability"):
            print(book)
# Buy function 
def buy():
    print(f"\nWhich book will you buy")
    buy_book = input("[buy]>> ")
    if buy_book in library_books:
        if library_books.get(buy_book).get("Availability"):
            print(f"""
The book {buy_book} is available. The info is listed below. 
{pd.Series(library_books.get(buy_book))}
Will You Buy?(y/n)""" )
            buy = input("[buy]>> ")
            if buy == "y":
                library_books[buy_book]["Stock"] -= 1
                print(f"""
The book {buy_book} of price {library_books.get(buy_book).get("price")}$ is out for delivery.^_^
HAPPY READING
For any query email us @sannslib@gmail.com""")
            else:
                print("Whenever you change your mind let us know - SannS Library ")
        else:
            print(f"""
The book {buy_book} is currently available
If you want you can pre-book it
For book details use "/info"
"""      )
            unavai = input("[pre-book]>>")
            if unavai == "/info":
                print(pd.Series(library_books.get(buy_book)))
                print("Will you Pre-Book:(y/n)")
                prbk = input("[pre-book]>>").lower
                if prbk == "y":
                    print("We will inform the sec the book appears to us")
                else:
                    print("Your wish!!")
            else:
                print("You can see our other books by cmd ='/list' ")
    else: 
        print(f"The book {buy_book} isnt available in our library or you might havr a typo (T.T)")


# Main Process 
print(WELCOME_TEXT)
user_input = ""
try:
     while user_input != "/exit":
        user_input = input(">>")
        if user_input == "/list":
             print("This books are available in our library")
             list_books()
        elif user_input == "/search":
            srch()
        elif user_input == "/help":
            print(HELP_TEXT)
        elif user_input == "/buy":
            buy()
        else:
             print("The command you typed didnt support.T_T")
     print(BYE_TEXT)
except KeyboardInterrupt:
     print("\n", BYE_TEXT)
