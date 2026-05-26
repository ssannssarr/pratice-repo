library_books = {
    "It Ends With Us":{
        "Availability": True,
        "price":99.5,
        "Author":"Collen Hoover",
        "Stock": 15
    }
} 

print(library_books.get("It Ends With Us"))









BUYBRRW="""
 Its available!!
 Will you buy or borrow?
 /buy = to buy
 /brrw = to borrow
 >> """
def list_t():
     print("Available")
     
     for book in library_books:
        if library_books[book].get("Availability"):
            print(book)
             

# List All Unvailable currently
def list_f():
    print("Unvailable")
    for book in library_books:
        if library_books[book].get("Availability") == False:
            print(book)