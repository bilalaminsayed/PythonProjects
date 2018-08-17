x = "y"

while x == 'y':
    number = int(input("Enter a number between 1-100: "))
    
    while number < 1 or number > 100:
        print("ERROR: the number cannot be less than 1 or greater than 100.")
        number = int(input("Enter the correct number: "))

    print(number)

    x = (input("Again? (y for yes) "))
