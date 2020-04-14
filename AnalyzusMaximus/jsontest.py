import json
import random
#class Catalog:

# for _ in range 

class Book:
    def __init__(self,author,title,year,ISBN):
        self.author = author
        self.title = title
        self.year = year
        self.ISBN = ISBN
        

def getCatalog(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)

myCatalog = getCatalog('./booksset1.json')

print(myCatalog)
len(myCatalog)
thisAuthor = myCatalog[1].get("author")
thisTitle = myCatalog[1].get("title")
thisYear = myCatalog[1].get("year")
thisISBN = '66666'
book1 = Book(thisAuthor,thisTitle,thisYear,thisISBN)

randomISBNmaker = random.choice(range(10000,99999))
print(randomISBNmaker)
print(book1.title)

# for x in len(myCatalog):
#     books[x] = Book()