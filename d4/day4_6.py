x = int(input('x = '))
y = int(input('y = '))

if x < y:   
    x, y = y, x

x0 = x
y0 = y

while x % y != 0:
    x, y = y, x % y
    if y==0:
        break 

print('%d和%d的最大公约数是%d' % (x0, y0, max(x,y)))
print('%d和%d的最小公倍数是%d' % (x0, y0, x0 * y0 / max(x,y)))