num = int(input("Enter a number: "))
result = 0
while num != 0:
    num //= 10
    result += 1
print("Result:", result)
