def myFirstFunc(name):
    print("Hello %s "  %(name))
myFirstFunc("Vijay")

def fulName(firstName,lastName):
    print("Hello %s %s" %(firstName,lastName))
fulName("Vijay","Patha")

def pathaFinance(income,saving,expense):
    return(income-saving-expense)
totalAccount = pathaFinance(100,35,50)
print(totalAccount)

# this is about scope fvar and sVar are within the function and hence cannot be reused outside the function
#however checkout the tVar, defined outside the funtion and hence can be reused
tVar = 10
def test():
    fVar = 10
    sVar = 20
    return fVar*sVar*tVar
print(test())
