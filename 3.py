outfile = open('numbers.txt', 'w')

for count in range(1, 201):
    outfile.write(str(count) + '\n')
    
outfile.close()
