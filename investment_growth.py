x = int(input("Enter the initial deposit amount: "))
p = int(input("Enter the annual interest rate percentage: "))
y = int(input("Enter the desired amount: "))

years = 0

while x < y:
    interest = (p / 100) * x
    x = x + interest
    years += 1

print("It will take years to reach the desired amount:", years)
