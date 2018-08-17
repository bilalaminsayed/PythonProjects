def main():
    number = get_number()
                       
    product = times_ten(number)

    print(product)

def get_number():
    return int(input("Enter a number: "))
    
def times_ten(number):
    return number * 10

main()

