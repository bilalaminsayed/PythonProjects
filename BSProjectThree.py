#Bilal Sayed 11/12/17
# This program demonstrates the MagicMachine class.
import magicmachine
def main():
        #creating an instance of magic machine
        barnesAndNoble = magicmachine.MagicMachine("Barnes and Noble", 5937, 251)
        #printing original inventory
        print(barnesAndNoble)
        #calling add books function
        barnesAndNoble.add_books(40)
        #calling add videos function
        barnesAndNoble.add_videos(91)
        #calling ship books function
        barnesAndNoble.ship_books(2436)
        #calling ship books function with a value that is out of range
        barnesAndNoble.ship_books(4392)
        #calling ship videos function
        barnesAndNoble.ship_videos(153)
        #calling ship videos function with a value that is out of range
        barnesAndNoble.ship_videos(591)
        #printing final inventory
        print(barnesAndNoble)
        # Create another instance of a Magic Machine store
        halfPriceBooks = magicmachine.MagicMachine("Half Price Books", 1486)
        #printing original inventory
        print(halfPriceBooks)
        #calling add books function
        halfPriceBooks.add_books(26)
        #calling add videos function
        halfPriceBooks.add_videos(82)
        #calling ship books function
        halfPriceBooks.ship_books(48)
        #calling ship books function with a value that is out of range
        halfPriceBooks.ship_books(3512)
        #calling ship videos function
        halfPriceBooks.ship_videos(21)
        #calling ship videos function with a value that is out of range
        halfPriceBooks.ship_videos(205)
        #printing final inventory
        print(halfPriceBooks)
        input()
# Call the main function
main()
