#Bilal Sayed 9/22/17

#Setting the range constants
LOW_TEMP = 0
HIGH_TEMP = 21
INCREMENT = 1

#Printing the table heading
print('Celsius\t\tFahrenheit')
print('-------------------------')

#Converting celsius to fahrenheit using the for loop
for celsius in range(LOW_TEMP, HIGH_TEMP, INCREMENT):
    #The conversion calculation
    fahrenheit = 1.8 * celsius + 32
    #Printing the results
    print(celsius, '\t\t', format(fahrenheit, '.1f'))
