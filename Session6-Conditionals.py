age = int(input("What is your age? "))

if age >=18: 
    print("Your age is {:d}". format(age))
    print("Adult!")
elif age >=6: 
    print("Your age is {:d}". format(age))
    print("Teenager!")
else: 
    print("Your age is {:d}".format(age))
    print("Baby!")

###################### BMI CALCULATOR #####################

weight = float(input("What is your weight in kg? "))
height = float(input("What is your height in cm? "))

def bmi_calc(weight, height):
    bmi = weight/((height/100)**2)

    if bmi >=30:
        print("Your BMI is {}.".format(bmi))
        print("Go run! You're obese ")
    elif bmi >=25:
        print("Your BMI is {}.".format(bmi))
        print("You are overweight!")
    elif bmi >=18.5:
        print("Your BMI is {}.".format(bmi))
        print("You are normal!")
    elif bmi <18.5:
        print("Your BMI is {}.".format(bmi))
        print("Eat more!")

bmi_calc(weight, height)

### Prof. Solution ###
# if bmi <= 18.5:
#     print("your bmi is {:f}. Underweight".format(bmi))
# elif bmi > 18.5 and bmi <= 25:
#     print("your bmi is {:f}. normal".format(bmi))
# elif 25 < bmi <= 29.9:
#     print("your bmi is {:f}. overweight".format(bmi))
# else:
#     print("your bmi is {:f}. obese".format(bmi))


########################## RECURSION ########################










