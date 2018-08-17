product = float(input('Enter a number: '))

while product < 100:
    product = 10 * product
    
    if product <= 100:
        print(product)
    else:
        print("")
