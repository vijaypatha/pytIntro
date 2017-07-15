'''
for x in range(0,3):
    print("hello Loops!")

todolist = ["Python 3 chapter","Data analysis","and","Business ideas"]
for x in todolist:
    print(x)
    #print x will print first x and then print J will print the rest
    for y in todolist:
        print(y)


for x in range(1,13):
    print x,
print()
print("-----------------------------------------------------")
for y in range(1,13):
    for z in range(1,13):
        print y*z,
    print("/n")
'''

'''
for x in range(0,3):
    print("Hello Loops")

todolist = ["python2Chapters","I'm about to finishi loops","data analysis", "etc"]
for x in todolist:
    print x,

for x in range(1,11):
    print x,
print()
print("--------------------------")
for y in range(1,11):
    for z in range(1,11):
        print y*z,
    print("/n")

#print even numbers
for x in range(1,100):
    if x % 2 == 0:
        print x,
#print odd numbers
for x in range(1,100):
    if x % 2 != 0:
        print x,
'''
'''
If you were standing on the moon right now, your weight would be 16.5 percent of what it is on Earth. You can calculate that by mul- tiplying your Earth weight by 0.165.
If you gained a kilo in weight every year for the next 15 years, what would your weight be when you visited the moon each year and at the end of the 15 years? Write a program using a for loop that prints your moon weight for each year.
'''
user = input("your weight")
float(user)
weight = int(float(user))
print user
moonWeg = 0.165*weight
print moonWeg
for x in range(1,16):
    incWeg = x + moonWeg
    print(incWeg)

#print odd numbers
for x in range(1,100):
    if x % 2 != 0:
        print x,
