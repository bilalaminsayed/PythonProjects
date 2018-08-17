#Bilal Sayed 9/29/17 Lab 5
# I dont know why the output is showing parentheses
#Main function
FAT_PERCENTAGE = 500 #25 of a 2000 calorie diet
CARB_PERCENTAGE = 1000 #50 of a 2000 calorie diet
PROTEIN_PERCENTAGE = 500 #25 of a 2000 calorie diet

def main():
    #get user input
    fat_grams = float(input("How many grams of fat did you eat today? "))
    carb_grams = float(input("How many grams of carbs did you eat today? "))
    protein_grams = float(input("How many grams of protein did you eat today? "))
    
    #call the functions
    fat = calories_from_fat(fat_grams)
    carbs = calories_from_carbs(carb_grams)
    protein = calories_from_carbs(protein_grams) #here i use the carb function
                                                 #because protein has the same amount
                                                 #of calories per gram
    #user input against constants to print later
    fat_remainder = FAT_PERCENTAGE - fat
    fat_over = fat - FAT_PERCENTAGE

    #user input against constants to print later
    carbs_remainder = CARB_PERCENTAGE - carbs
    carbs_over = carbs - CARB_PERCENTAGE

    #user input against constants to print later
    protein_remainder = PROTEIN_PERCENTAGE - protein
    protein_over = protein - PROTEIN_PERCENTAGE

    #see if the user is over or under daily values
    if fat < FAT_PERCENTAGE:
        fat_message = ('which is', fat_remainder, 'calories less than the daily value for a 2000 calorie diet.')
    else:
        fat_message = ('which is', fat_over, 'calories more than the daily value for a 2000 calorie diet.')
    if carbs < CARB_PERCENTAGE:
        carbs_message = ('which is', carbs_remainder, 'calories less than the daily value for a 2000 calorie diet.')
    else:
        carbs_message = ('which is', carbs_over, 'calories more than the daily value for a 2000 calorie diet.')

    if protein < PROTEIN_PERCENTAGE:
        protein_message = ('which is', protein_remainder, 'calories less than the daily value for a 2000 calorie diet.')
    else:
        protein_message = ('which is', protein_over, 'calories more than the daily value for a 2000 calorie diet.')
        
    #total calculation
    total_calories = fat + carbs + protein
                       
    #display the result
    print("You ate ", fat, "calories of fat,", fat_message)
    print("You ate ", carbs, "calories of carbs,", carbs_message)
    print("You ate ", protein, "calories of protein,", protein_message)
    print("Your total calories for today are ", total_calories, "/2000 calories")

#define the fat fucntion    
def calories_from_fat(grams):
    return grams * 9

#define the carbs fucntion
def calories_from_carbs(grams):
    return grams * 4

#execute the main function
main()
