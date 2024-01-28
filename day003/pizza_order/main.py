print("Hi. Welcome to Python Pizza.")
size = input("Please type S for Small, M for Medium or L for Large.\n").lower()
pepperoni = input("Would you like pepperoni? Please type Y for Yes or N for No.\n").lower()
cheese = input ("Would you like extra cheese? Please tupe Y for Yes or N for No.\n").lower()

total = 0

if size == "s":
    total += 15
elif size == "m":
    total += 20
else:
    total += 25

if pepperoni == "y" and size == "s":
    total += 2
elif pepperoni == "y" and size == "m":
    total += 3
elif pepperoni == "y" and size == "l":
    total += 3

if cheese == "y":
    total += 1

print(f"Your final bill is ${total}. Thank you.")