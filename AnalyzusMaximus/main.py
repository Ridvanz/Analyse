import json




class Person:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

class Book:
    def __init__(self,author,title,year):
        self.author = author
        self.title = title
        self.year = year

class Catalog:
    def __init__(self, books):
        self.books = books
    def addBook(self, book):
        self.books.append(book) 
    def remBook(self, book):    
        self.books.remove(book) 


class Subscriber(Person):
    def __init__(self, name, ID):
        super().__init__(name, ID)

class PublishingCompany(Person):
    def __init__(self, name, ID):
        super().__init__(name, ID)

class Librarian(Person):
    def __init__(self, name, ID):
        super().__init__(name, ID)

class LoanAdministration:
    def __init__(self, name, ID):
        self.customers = customers
        self.ID = ID

    def addCustomer(self):

        1+1
        # def customerINFO():
            
        #     global customerID, customers
        #     customerID += 1
        #     customers.append(customerID)
        #     newName = input("\n"*50 + "Enter the new customer's name: ")
            
        #     return newName

        # typeOfCustomer = input("\n"*50 + "Enter a number according to what you want to do next.\n\n 1. Add a new Subscriber \n 2. Add a new Publishing Company \n 3. Go back to main menu\n" + "\n"*10)
        # while typeOfCustomer not in {'1','2','3'}:
        #     print("Invalid input, please enter either '1', '2' or '3'")
        #     typeOfCustomer = input("Enter a number according to what you want to do next.\n\n 1. Add a new Subscriber \n 2. Add a new Publishing Company \n 3. Go back to main menu\n" + "\n"*10)
        
        # if typeOfCustomer == '1':
        #     customerName = customerINFO()
        #     customers[customerID] = Subscriber(customerName,customerID)
        #     print("New subscriber '{}' has ID: {}".format(customerName,customerID))
        # elif typeOfCustomer == '2':
        #     customerName = customerINFO()
        #     customers[customerID] = PublishingCompany(customerName,customerID)
        #     print("New publishing company '{}' has ID: {}".format(customerName,customerID))
        




########################################################################################################
# running = True
# while running == True:


def getCatalog(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)

cat = Catalog([])

myCatalog = getCatalog('./booksset1.json')

# for x in myCatalog:
#     cat.books.append(Book(x.get("author"),x.get("title"),x.get("year")))

for x in myCatalog:
    cat.addBook(Book(x.get("author"),x.get("title"),x.get("year")))


# print(cat.books[20].author)
# print(len(cat.books))
# len(myCatalog)


print("\n"*20+"\n\n"+"="*43 + "\n>  Welcome to the Public Library System!  <\n" + "="*43 + "\n"*3)

Usertype = None
while Usertype not in {'1','2','3'}:
    print('Invalid input, please enter either "1", "2" or "3"')
    Usertype = input("Enter a number according to your account.\
                \n\nAre you\
                \n 1. A Subscriber?\
                \n 2. A Publishing Company?\
                \n 3. A Librarian?\n\n"\
                + "\n"*5)

if Usertype == '1':
    User = Subscriber("name",0)
elif Usertype == '2':
    User = PublishingCompany("Publishing Company",0)  
elif Usertype == '3':
    User = Librarian("Librarian",0)

print("\n"* 50 + "~"*30 + "\n\n\n" + "Logged in as a {}".format(User.name) + "\n\n\n" +"~"*30 + "\n"*5)

while True:
    nextFunction = input("What do you want to do?\n\n\
Enter '1' to search for a book\n\
Enter '2' to loan a book\n\
Enter '3' to add a new customer\n\
Enter '4' to add a new book item\n\
Enter '5' to make a backup of the data in the system\n\
Enter '6' to restore library from backup\n\
Enter '7' to log out\n"\
+ "\n" * 5)
                    
    if nextFunction == "1":
        print("1")
    elif nextFunction == "2":
        print("2")
    elif nextFunction == "3":
        lib.addCustomer()
    elif nextFunction == "4":
        print("4")
    elif nextFunction == "5":
        print("5")
    elif nextFunction == "6":
        print("6")
    elif nextFunction == "7":
        print("7")
        break

    


