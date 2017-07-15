'''
import time
print(time.asctime())

import sys
print(sys.stdin.readline())
'''
'''
import sys
def findAge():
    print("How old are you?")
    age = int(sys.stdin.readline())
    if age > 10:
        print("too old to be happy!")
    else:
        print("rats!, you again!")
findAge()

def makeCall():
    print("How old are you?")
    age=int(sys.stdin.readline())
    if age > 10:
        print("too old to be happy")
    else:
        print("cats! and dogs!")
makeCall()
'''

import sys
def moonweg():
    print("what is your weight on earth?")
    wegMoon = int(sys.stdin.readline())*0.165
    print("your weight on moon %s" %wegMoon)
    print("weight increase in future?")
    wegInc = (sys.stdin.readline())
    for x in range(wegInc,16):
        newWeg = x + wegMoon
        print newWeg,
moonweg()
