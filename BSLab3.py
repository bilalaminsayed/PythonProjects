#Bilal Sayed 9/15/17
#This program is to display shipping charges
#Shipping charges
LIGHT = 1.50
MEDIUM = 3.00
HEAVY = 4.00
FREIGHT = 4.75

#Get weight
weight = float(input('Enter weight of package(lbs): '))

#Calculate the shipping charges
if weight > 10:
    shipping = weight * FREIGHT
elif weight <= 10 and weight > 6:
    shipping = weight * HEAVY
elif weight <= 6 and weight > 2:
    shipping = weight * MEDIUM
else:
    shipping = weight * LIGHT
    
#Display the shipping cost
print('Your shipping total is $', format(shipping, ',.2f'), sep='')
input()




                     
