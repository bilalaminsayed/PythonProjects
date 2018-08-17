#Bilal Sayed 11/12/17
#create magicmachine class
class MagicMachine:
    #define init with books and videos defaulting to 0
    def __init__(self, name, books=0, videos=0):
        self.__name = name
        self.__books = books
        self.__videos = videos
    #define add books which adds books to inventory    
    def add_books(self, books):
        print('Adding', books, 'books to stock.')
        self.__books += books
        print('Updated stock:', self.__books)
    #define add videos which adds videos to inventory    
    def add_videos(self, videos):
        print('Adding', videos, 'videos to stock.')
        self.__videos += videos
        print('Updated stock:', self.__videos)
    #define ship books which checks the argument against the current value. If the argumentit is larger than the current value, it prints an error message.    
    def ship_books(self, books):
        if books < self.__books:
            print('Removing', books, 'books from stock.')
            self.__books -= books
            print('Updated stock:', self.__books)
        else:
            print('Error: Not enough stock. You want to ship ', books, 'books, but there are only ', self.__books, 'in stock.')
    #define ship videos which checks the argument against the current value. If the argumentit is larger than the current value, it prints an error message.        
    def ship_videos(self, videos): 
        if videos < self.__videos:
            print('Removing', videos, 'videos from stock.')
            self.__videos -= videos
            print('Updated stock:', self.__videos)
        else:
            print('Error: Not enough stock. You want to ship', videos, 'videos, but there are only', self.__videos, 'in stock.')
    #define str which prints out the inventory when print() is called
    def __str__(self):
        return '\nStore: ' + str(self.__name) + '\nBooks: ' + str(self.__books) + '\nVideos: ' + str(self.__videos) + '\n'
