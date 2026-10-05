num = int(input("Enter a number: "))

original = num
digits = 0
temp = num

while temp > 0:
    digits = digits + 1
    temp = temp // 10

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** digits
    temp = temp // 10

if sum == original:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")