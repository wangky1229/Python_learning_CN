import time
import sys

class Clock(object):
    """"数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        """"Initialization method""

         :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second
    
    def run(self):
        """running"""
        self._second +=1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0
    
    def show(self):
        """"visualization"""
        return '%02d:%02d:%02d' % \
                (self._hour, self._minute, self._second)

def main():
    h,m,s=map(int,input("Enter the actuel time(h m s separated by space): ").split())
    clock = Clock(h,m,s)
    while True:
        print('\r', clock.show(), flush=False ,end='')
        time.sleep(1)
        clock.run()

if __name__ == '__main__' :
    main()