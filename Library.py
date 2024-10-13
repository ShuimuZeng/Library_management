#https://www.geeksforgeeks.org/hotel-management-system/
class Books:
    sort_parameter = 'name'
    def __init__(self) -> None:
        self.name = ''
        self.queue_number = 0
        self.location = ''
        # self.rating = int
        # self.pricePr = 0
        self.current_holder = ''
    def __lt__(self, other):
        getattr(self, Books.sort_parameter) < getattr(other, Books.sort_parameter)
    # Function to change sort parameter to
    # name
    @classmethod
    def sortByName(cls):
        cls.sort_parameter = 'name'

    # Function to change sort parameter to
    # rating.
    @classmethod
    def sortByqueueNum(cls):
        cls.sort_parameter = 'queue_number'

    # Function to change sort parameter to
    # room availability.

    # @classmethod
    # def sortByRoomAvailable(cls):
    #     cls.sortParam = 'roomAvl'

    def __repr__(self) -> str:
        return "BOOKS DATA:\nBook_Name:{}\tQueue number:{}\tLocation:{}\tCurrent_holder:{}".format(
            self.name, self.queue_number, self.location,self.current_holder)

class Students:
    def __init__(self) -> None:
        self.student_name = ''
        self.student_id = ''
        self.book_holding = ''

    def __repr__(self) -> str:
        return "UserName:{}\tUserId:{}\tBook Holding Now:{}".format(self.student_name, self.student_id, self.book_holding)

    # Print Books data.
def PrintBookData(books):
    for h in books:
        print(h)

    # Sort Hotels data by name.
def SortBookByName(books):
    print("SORT BY NAME:")

    Books.sortByName()
    books.sort()

    PrintBookData(books)
    print()

#print where the book is
def PrintBookLocation(s,books):
    print("BOOKS FOR {} LOCATION ARE:".format(s))
    Location_of_book = [h for h in books if h.location == s]

    PrintBookData(Location_of_book)
    print()
    return 0

# Sort hotels by room Available.
def SortByqueueNum(books):
    print("SORT BY ROOM AVAILABLE:")
    Books.sortByqueueNum()
    books.sort()
    PrintBookData(books)
    print()

# Print the user's data
def PrintUserData(userName, userId, bookholding, books):
    users = []
    # Access user data.
    for i in range(3):
        u = Students()
        u.student_name = userName[i]
        u.student_id = userId[i]
        u.book_holding = bookholding[i]
        users.append(u)

    for i in range(len(users)):
        print(users[i], "\tHotel name:", books[i].name)


# Function to solve
# Hotel Management problem
def BookManagement(userName,
                    userId,
                    bookName,
                    queue_num,
                    book_holding,
                    locations,
                    current_holder
                    ):
    # Initialize arrays that stores
    # hotel data and user data
    books = []

    # Create Objects for
    # hotel and user.

    # Initialise the data
    for i in range(3):
        h = Books()
        h.name = bookName[i]
        h.queue_number = queue_num[i]
        h.location = locations[i]
        h.current_holder = current_holder[i]
        #h.pricePr = prices[i]
        books.append(h)

    print()

    # Call the various operations
    PrintBookData(books)
    SortBookByName(books)
    SortByqueueNum(books)
    PrintBookLocation("Bangalore",
                     books)
    #SortByRoomAvailable(books)
    PrintUserData(userName,
                  userId,
                  book_holding,
                  books)


# Driver Code.
if __name__ == '__main__':
    # Initialize variables to stores
    # hotels data and user data.
    userName = ["U1", "U2", "U3"]
    userId = [2, 3, 4]
    BookName = ["H1", "H2", "H3"]
    #bookingCost = [1000, 1200, 1100]
    queue_waiting = [4, 5, 6]
    locations = ["Bangalore",
                 "Bangalore",
                 "Mumbai"]
    # ratings = [5, 5, 3]
    # prices = [100, 200, 100]
    currentholder = ["U1", "U2", "U3"]
    book_holding = ["H1", "H2", "H3"]
    # Function to perform operations
    BookManagement(userName, userId,
                    BookName,queue_waiting, book_holding,locations,currentholder)