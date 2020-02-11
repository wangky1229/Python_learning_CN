import math
ran = int(input('请输入搜索范围'))
counter=0

for i in range(5, ran ,1):
    s=0

    search_range = int(math.sqrt(i))

    if  i % search_range == 0 and i / search_range == search_range: 
            s+= search_range

                

    for j in range (1, search_range ,1):
        if i % j ==0 and i/j != j:
            s+= j
            s+= i /j
    s-=i
    if s == i:
        counter += 1
        print('第%d完全数是%d' % (counter, i),end='\n')

print('范围%d内完全数有%d个' % (ran, counter),end='\n')
