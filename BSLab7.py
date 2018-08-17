def main():
    
    months = ('January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'Ooctober', 'November', 'December')
    rainfall = []
    total = 0

    for m in months:
        rainfall.append(float(input('What was the rainfall in ' + m + '? ')))
        
    for num in rainfall:
            total += num
    avg = total / 12
    
    print('The total rainfall was ', total)
    print('The average rainfall was ', avg)
    print('The month with the higest rainfall was ', months[rainfall.index(max(rainfall))])
    print('The month with the lowest rainfall was ', months[rainfall.index(min(rainfall))])    

    input()
    
main()
