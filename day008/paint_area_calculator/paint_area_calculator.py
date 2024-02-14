# Write your code below this line 👇
test_h = int(input("What's the height of the wall?\n")) # Height of wall (m)
test_w = int(input("What's the width of the wall?\n")) # Width of wall (m)
coverage = 5

cans = round((test_h*test_w)/coverage)

def paint_calc(height, width, cover):
    print(f"You'll need {cans} cans of paint.")
paint_calc(height=test_h, width=test_w, cover=coverage)
# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
