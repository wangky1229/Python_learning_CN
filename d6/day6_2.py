def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

print(is_palindrome(123454321))
for i in range(2,20,1):
    print(i,end='\n')
