#Bilal Sayed 11/10/17 Lab 11
#create employee class
class Employee:
    def __init__(self, emp_name, emp_number):
        self.__emp_name = emp_name
        self.__emp_number = emp_number
        
    def set_emp_name(self, emp_name):
        self.__emp_name = emp_name
        
    def set_emp_number(self, emp_number):
        self.__emp_number = emp_number

    def get_emp_name(self):
        return self.__emp_name

    def get_emp_number(self):
        return self.__emp_number
#create production worker subclass
class ProductionWorker(Employee):
    def __init__(self, emp_name, emp_number, shift_num, wage):
        Employee.__init__(self, emp_name, emp_number)
        self.__shift_num = shift_num
        self.__wage = wage
        
    def set_shift_num(self, shift_num):
        self.__shift_num = shift_num

    def set_wage(self, wage):
        self.__wage = wage

    def get_shift_num(self):
        if self.__shift_num == 1:
            return 'Day shift'
        else:
            return 'Night shift'

    def get_wage(self):
        return self.__wage
            
def main():
    #get name
    emp_name = (input('Enter employee name: '))
    #get number
    while True:
        try:
            emp_number = int(input('Enter employee number: '))
        except ValueError:
           print('Error: Not a number. Please try again.')
        else:
            break
    #get shift num
    while True:
        try:
           shift_num = int(input('Enter shift number (1 for day or 2 for night): '))
        except ValueError:
           print('Error: Not a number. Please try again.')
        else:
           if 1 <= shift_num <= 2:
               break
           else:
               print('Error: Please enter a 1 for day or 2 for night')
    #get wage
    while True:
        try:
           wage = float(input('Enter wage: '))
        except ValueError:
           print('Error: Not a number. Please try again.')
        else:
            break
    #create object           
    worker = ProductionWorker(emp_name, emp_number, shift_num, wage)

    #print data
    print('Data Entered:')
    print('Employee name:', worker.get_emp_name())
    print('Employee number:', worker.get_emp_number())
    print('Employee shift:z', worker.get_shift_num())
    print('Employee wage: $', format(worker.get_wage(), ',.2f'), sep='')
    


main()
