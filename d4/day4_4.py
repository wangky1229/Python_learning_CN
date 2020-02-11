import math

num=int(input('请输入正整数：'))
end=int(math.sqrt(num))
is_prime=True
for x in range(2,end+1):
    if num % x== 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是质数' % num)
else:
    print('%d不是质数' % num) 

