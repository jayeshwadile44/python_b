#Use a while loop to reverse a given number ( eg. 123-->321)
num = 123
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
print(reversed_num)