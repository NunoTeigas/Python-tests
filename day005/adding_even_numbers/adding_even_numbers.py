target = int(input("Enter a number between 0 and 1000.\n"))
sum_even = 0
for even in range(2, target +1, 2):
    sum_even += even
print(sum_even)
