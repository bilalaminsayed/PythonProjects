#Bilal Sayed 11/17/17 Lab 12
def main():
    #get input
    x = int(input('Enter a number for x: '))
    y = int(input('Enter a number for y: '))
    #call funtion and display result
    print(multiply(x, y))
#create multiply function
def multiply(x, y):
    #state the base case
    if x == 0 or y == 0:
        return 0
    #recursively call the function
    else:
        return x + multiply(x, y-1)

main()
        
        
