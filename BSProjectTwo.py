#Bilal Sayed 10/22/17 Project 2
def main():
    #import for final file timestamp
    import datetime
    #while loop for file input verification
    while 1:
        #try/catch for file not found error
        try:
            infile_name = input('Enter the file name: ')
            #open file
            infile = open(infile_name, 'r')
            break
        except FileNotFoundError:
            print('File not found. Make sure file exists and try again')
    #read file
    infile_read = infile.read()
    #strip any extra spaces or newline characters
    infile_strip = infile_read.strip()
    #spilt file into list
    infile_split = infile_strip.split('\n')
    #find number of items in file
    file_items = 0
    for ch in infile_split:
        file_items += 1
    #loop to test if number is 16 digits long and store results in a list
    length_list = []
    correct_length = False
    for ch in infile_split:
        if len(ch) == 16:
            correct_length = True
        else:
            correct_length = False
        length_list.append(correct_length)
    #loop to put each number through the algorithm    
    correct_value_list = []
    valid_list = []
    valid = False
    #first test to see if number is 16 digits long
    for ch in infile_split:
        if len(ch) == 16:
            num0 = (int(ch[0]) *2)
            if num0 >= 9:
                num0 = num0 - 9
            num1 = int(ch[1])
            num2 = (int(ch[2]) * 2)
            if num2 >= 9:
                num2 = num2 - 9
            num3 = int(ch[3])
            num4 = (int(ch[4]) * 2)
            if num4 >= 9:
                num4 = num4 - 9
            num5 = int(ch[5])
            num6 = (int(ch[6]) * 2)
            if num6 >= 9:
                num6 = num6 - 9
            num7 = int(ch[7])
            num8 = (int(ch[8]) * 2)
            if num8 >= 9:
                num8 = num8 - 9
            num9 = int(ch[9])
            num10 = (int(ch[10]) * 2)
            if num10 >= 9:
                num10 = num10 - 9
            num11 = int(ch[11])
            num12 = (int(ch[12]) * 2)
            if num12 >= 9:
                num12 = num12 - 9
            num13 = int(ch[13])
            num14 = (int(ch[14]) * 2)
            if num14 >= 9:
                num14 = num14 - 9
            num15 = int(ch[15])
            #add up all the numbers 
            num_master = (num0 + num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8
                           + num9 + num10 + num11 + num12 + num13 + num14 + num15)
            #test if they are a multiple of 10
            test = num_master%10
            if test == 0:
                valid = True
            else:
                valid = False
            #store results in a list
            valid_list.append(valid)
            #finding value to correct invalid numbers
            if valid == False:
                correction_total = (num0 + num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8
                               + num9 + num10 + num11 + num12 + num13 + num14)
                correction_value = 10 - (correction_total%10)
                #add corrected number to a list
                correct_value_list.append(correction_value)
            else:
                correct_value_list.append(0)
        else:
            valid = False
            valid_list.append(valid)
            correct_value_list.append(valid)
    #loop to add up  all the valid and invalid numbers       
    accepted = 0
    denied = 0
    for ch in valid_list:
        if ch == True:
            accepted += 1
        else:
            denied += 1    
    #create outfile
    outfile = open('credit_card_numbers_report.txt', 'w')
    outfile.write('Credit Card Number Report\n')
    outfile.write('Bilal Sayed ')
    #write timestamp
    outfile.write('| {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
    outfile.write('\n')
    #write records read
    outfile.write(str(file_items))
    outfile.write(' records read\n')
    #write number of valid numbers
    outfile.write(str(accepted))
    outfile.write(' valid records\n')
    #write number of invalid numbers
    outfile.write(str(denied))
    outfile.write(' invalid records\n')
    outfile.write('\n')
    #loop to write the results to the file
    for i in range(len(infile_split)):
        if length_list[i] == True:
            if valid_list[i] == True:
                outfile.write('Card number ')
                outfile.write(infile_split[i])
                outfile.write(' is a Valid credit card number.\n')
            else:
                outfile.write('Card number ')
                outfile.write(infile_split[i])
                outfile.write(' is Not Valid. ')
                outfile.write('The last digit should be ')
                outfile.write(str(correct_value_list[i]))
                outfile.write('.\n')
        else:
            outfile.write('            ')
            outfile.write('%-16s' % infile_split[i])
            outfile.write(' is not a credit card number.\n')
    #console output of number of recors read and their validity
    print('A total of ', file_items, ' records were read')
    print(accepted, 'were valid card numbers and ', denied, 'were invalid card numbers.')
    #close the files
    infile.close()
    outfile.close()
    input()
main()






























