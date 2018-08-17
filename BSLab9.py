#Bilal Sayed 10/27/17
def main():
    #initialize dictionaries
    roomNumber = {'CS101':3004, 'CS102':4501, 'CS103':6755, 'NT110':1244, 'CM241':1411}
    courseInstructor = {'CS101':'Haynes', 'CS102': 'Alvarado', 'CS103':'Rich', 'NT110':'Burke', 'CM241':'Lee'}
    meetingTime = {'CS101':'8:00 a.m.', 'CS102':'9:00 a.m.', 'CS103':'10:00 a.m.', 'NT110':'11:00 a.m.', 'CM241':'1:00 p.m.'}
    #print the courses availible by running a for loop on one dictionary with the keys method and make a list to help with input validation
     print('Current courses: ')
    courses = []
    for key in roomNumber.keys():
        print(key)
        courses.append(key)
    #get the user input    
    courseNumber = input('Enter a course number: ').upper()
    #input validation with while loop
    while courseNumber not in courses:
        courseNumber = input('Course not found. Try again: ').upper()
    #print output    
    print()
    print('Course', courseNumber)
    print('Room #:', roomNumber[courseNumber])
    print('Instructor:', courseInstructor[courseNumber])
    print('Meeting time:', meetingTime[courseNumber])
main()
