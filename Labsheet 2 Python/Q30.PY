num = int(input("Enter a number: "))

original = num
sum = 0

while num > 0:
    digit = num % 10

    factorial = 1

    for i in range(1, digit + 1):
        factorial = factorial * i

    sum = sum + factorial
    num = num // 10

if sum == original:
    print("The number is a strong number.")
else:
    print("The number is not a strong number.")