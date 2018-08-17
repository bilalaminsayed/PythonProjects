#Bilal Sayed 11/3/17
#create class Car
class Car:
    #define initialization method
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    #define accerate method
    def accelerate(self):
        self.__speed += 5
    #define brake method
    def brake(self):
        self.__speed -= 5
    #define get_speed method
    def get_speed(self):
        return self.__speed
    #define get_year method
    def get_year_model(self):
        return self.__year_model
    #define get_make method    
    def get_make(self):
        return self.__make
    #define string method    
    def __str__(self):
        return 'The current speed is ' + str(self.__speed) + ' mph.'
#Define main
def main():
    #get year
    year_model = input('Enter the model year: ')
    #get make    
    make = input('Enter the make: ')
    #create car object
    car = Car(year_model, make)
    #print object make and year
    print('The car is a', car.get_year_model(), car.get_make())
    #increase speed 5 times and print result each time
    for count in range(5):
        car.accelerate()
        print(car)
    #decrease speed 5 times and print result each time
    for count in range(5):
        car.brake()
        print(car)

main()
