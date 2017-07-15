#Problem 1 - Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
name = raw_input("Name ?")
age = raw_input("age ?")
year = 2016 - int(age) + 100
print(name, "will be 100 in year", year)

#name = input("Name?")
#age = int(input("Age?"))
#year = 2016 - age + 100
#print(name,"will be 100 in year", year)


#####################################

#Problem 2 - Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

#num = raw_input("enter Number ")
#x = int(num) % 2
#if x > 0:
#    print("the number is odd")
#else:
#     print("the number is even")

num = int(input("Enter a Number"))
x = num % 2
if x > 0:
	print("the number is odd")
else:
	print("the number is even")
#####################################
#Problem 3  write a program that prints out all the elements of the list that are less than 5.
