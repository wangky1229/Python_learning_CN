import math
a = 154476802108746166441951315019919837485664325669565431700026634898253202035277999
b = 36875131794129999827197811565225474825492979968971970996283137471637224634055579
c = 4373612677928697257861252602371390152816537558161613618621437993378423467772036
s=a/(b+c)+b/(a+c)+c/(a+b)
print('答案: %.2f' % s)