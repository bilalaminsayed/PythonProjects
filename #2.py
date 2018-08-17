keep_going = 'y'

while keep_going == 'y' or keep_going == 'Y':
    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))

    answer = first + second

    print(answer)

    keep_going = input("Do you want to calculate another
                       number? (Enter y for yes) ")
