# 1st input: enter height in meters e.g: 1.65
height = input("Please enter your height in meters (use the full stop as a decimal separator).\n")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("Please enter your weight in kilograms.\n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

#bmi = int(int(weight)/float(height)**2) #Alternative way line I
#print(f"Your BMI is {bmi}.") #Alternative way line II

print(f"Your BMI is {int(int(weight)/float(height)**2)}")