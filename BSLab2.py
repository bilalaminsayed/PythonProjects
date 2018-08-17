#This program is to calculate MPG 
#Get miles driven
miles_driven = float(input('Enter the miles driven: '))

#Get gallons of gas used
gallons_used = float(input('Enter the gallons of gas used: '))

#Calculate MPG and assign it to MPG
MPG = (miles_driven / gallons_used)

#Display the MPG
print('Your car gets',
      format(MPG, ',.1f'), 'miles-per-gallon')
input()
