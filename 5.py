infile = open('number_list.txt', 'r')

total = 0.0

count = 0
for line in infile:
    number = float(line)
    count += 1
    total += number

infile.close()

print(total)
