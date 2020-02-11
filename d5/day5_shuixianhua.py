import math

counter = int(0)

for i in range(1,9,1):
    for j in range(1,9,1):
        for k in range(1,9,1):
            if math.pow(i, 3) + math.pow(j, 3)  + math.pow(k, 3)  == i*100 + j*10 + k:
                counter += 1
                print('第%d个水仙花数为：%d' % (counter, i * 100 + j * 10 + k), end ='\n')


print('共有水仙花数%d个' % (counter))    