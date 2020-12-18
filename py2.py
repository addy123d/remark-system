# Conditional statements !
# Problem statement - Aditya wants to purchase burger of Rs 120 and he has 80
# Condition for buying burger - if he has 120 rs or greater than 120

# 1. Calculate percentage and remark them !

# a. take marks as an input !
name = input("Enter your name : ")
subject_1 = int(input("Enter marks of subject-1 : "))
subject_2 = int(input("Enter marks of subject-2 : "))
subject_3 = int(input("Enter marks of subject-3 : "))
subject_4 = int(input("Enter marks of subject-4 : "))

# b. Calculate percentage
if subject_1 <= 100 and subject_2 <= 100 and subject_3 <= 100 and subject_4 <= 100:

    total = subject_1 + subject_2 + subject_3 + subject_4
    print(f'Total : {total}')

    percentage = (total/400) * 100

    print(f'Percentage% : {percentage}')

    # c. Give them remarks as per percentage !
    # Conditions :
    # 1. Greater than 80 - Excellent !
    # 2. Greater than 70 but less than or equals to 80 - Very Good !
    # 3. Greater than 50 but less than or equals to 70 - Good !
    # 4. Anyone below 50 - Needs to improve !

    if percentage > 80:
        # Give remark !
        print(f"{name} has performed EXCELLENT in this exams !")
    elif percentage <= 80 and percentage > 70:
        # Give remark !
        print(f"{name} has performed VERY GOOD in this exams !")
    elif percentage <= 70 and percentage > 50:
        # Give remark !
        print(f"{name} has performed GOOD in this exams !")
    else:
        print(f"{name} needs to improve :( !")

else:
    print("Invalid Input !")
