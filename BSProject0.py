#This program is to calculate obtains the number of Reserved Seating
#tickets that have been sold for a recent event and totals their revenue

#Get number of silver tickets sold
silver = float(input('  Enter the number of Silver tickets sold: ',))

#Get number of gold ticket sold
gold = float(input('    Enter the number of Gold tickets sold: ',))

#Get number of platinum tickets sold
platinum = float(input('Enter the number of Platinum tickets sold: '))

#Calculate the total number tickets and assign it to total
total = float(silver + gold + platinum)

#Calculate the total revenue of the silver tickets and assign it to silver_total
silver_total = float(silver * 35.00)

#Calculate the total revenue of the gold tickets and assign it to gold_total
gold_total = float(gold * 55.00)

#Calculate the total revenue of the platinum tickets sold and assign it to platinum_total
platinum_total = float(platinum * 85.00)

#Calculate total revenue and assign it to total_revenue
total_revenue = float(silver_total + gold_total + platinum_total)

#Display the totals
print()
print('Section', 'Tickets', 'Revenue', sep='  ')
print('-------- -------  -------')
print('  Silver', format(silver, '7.0f'), end='')
print('  $', format(silver_total, '2,.0f'), sep='')
print('    Gold', format(gold, '7.0f'), end='')
print('  $', format(gold_total, ',.0f'), sep='')
print('Platinum', format(platinum, '7.0f'), end='')
print('  $', format(platinum_total, ',.0f'), sep='')
print('======== =======  =======')
print('   Total', format(total, '7.0f'), end='')
print('  $', format(total_revenue, ',.0f'), sep='')

input()
