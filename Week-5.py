class book():
    type = "Jotter"
    function = "For noting key points"

    def myBook(self):
        print("My book is very important to me")

    def __init__(self, ownerName, coverType):
        self.ownerName = ownerName
        self.coverType = coverType
        self.__pages = 100 #private attributes to demonstrate Encapsulation

    def get_pages(self):
        return self.__pages #Give what is defined at the top
    
    def add_pages(self, count_PagesToBeAdded):
        if count_PagesToBeAdded > 0:
            self.__pages += count_PagesToBeAdded
            print(f"✅Added {count_PagesToBeAdded} pages. Total pages now is: {self.__pages}")
        else:
            print(f"Invalid number of pages to add.")

#Child class (inherits from Book
class Notebook(book):
    def __init__(self, ownerName, coverType, subject):
        super().__init__(ownerName, coverType)
        self.subject = subject
    def describe(self):
        print(f"Notebook owned by: {self.ownerName} for: {self.subject} with a: {self.coverType} cover.")
        #This print take every self. that has been defined above

# Create object
theBook = Notebook("Alabi Sunday Elisha", "Hardcover", "Python Programming")
theBook.myBook()
theBook.describe()
print(f"Total pages:", theBook.get_pages())
theBook.add_pages(50)

#Polymorphism Challenge!
class car():
    def travel_medium(self):
        return f"The medium of travel is: Land"
class plane():
    def travel_medium(self):
        return f"The medium of travel is: Air"
class ship():
    def travel_medium(self):
        return f"The medium of travel is: Water" 
for vehicles in [car(), plane(), ship()]:
    print(vehicles.travel_medium())
