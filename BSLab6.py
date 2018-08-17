def main():
    infile = open('numbers.txt', 'r')

    total = 0.0

    count = 0
    for line in infile:
        number = float(line)
        count += 1
        total += number
        avg = (total / count)

    infile.close()

    print('The average is', avg)
    

main()
