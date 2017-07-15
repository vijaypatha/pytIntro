toDoList = ["python","dataanalytics","watchlessTV"]
print(toDoList[0])
print(toDoList[0:2])
print(toDoList[0:3])
other_toDo = ["haircut","visit ksl","somethingelse"]
allToDo = [toDoList,other_toDo]
#print(allToDo)
print(allToDo[1][1])
print(allToDo[0][2])
toDoList.append('rats')
print(toDoList)
toDoList.insert(0,"findhappiness")
print(toDoList)
print(len(toDoList))
print(len(allToDo))
