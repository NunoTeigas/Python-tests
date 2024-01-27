height = float(input("Type your height in meters.\n"))
weight = int(input("Type your weight in kilograms.\n"))
bmi = weight/(height**2)
#print(int(bmi))
if bmi < 18.5:
    print(f"{bmi}, you are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print(f"{bmi}, you have a normal weight.")
elif bmi >= 25 and bmi < 30:
    print(f"{bmi}, you are slightly overweight.")
elif bmi >= 30 and bmi < 35:
    print(f"{bmi}, you are obese.")
else:
    print(f"{bmi}, you are clinically obese.")