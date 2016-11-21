fruitList = ["apple", "orange","banana","grape","tomato","mango"]
print (fruitList[-2])

numberList1 = [1,2,3]
numberList2 = [6,7,8]
numberList3 = numberList1 + numberList2

print(numberList3*3)

print (fruitList[2:5])
print (fruitList[:4])
print (fruitList[:])
fruitList[1] = "Kiwi"
print (fruitList)

olympiclist = (["London", 2012], ["Beijing",2008], ["Athens",2004])

print (olympiclist)
print (olympiclist[1])
print (olympiclist[1] [0])

inventorylist = ["sword", "armor", "shield", "healing postion"]
inventorylist.append("cabbage")
inventorylist.insert(2,"cabbage")
print (inventorylist)

inventorylist.sort()
print (inventorylist)

print(inventorylist.count("sword"))

inventorylist.extend(fruitList)

print(inventorylist)
print (fruitList)

vfruit = fruitList.pop()
print (fruitList)
print(vfruit)

vfruit = fruitList.pop(0)
print (fruitList)
print(vfruit)

fruitList.remove("banana")
print(fruitList)

fruitList.reverse()
print(fruitList)

fruitList = ["apple", "orange","banana","grape"]
vindex = fruitList.index("banana")
print (vindex)

print(len(fruitList))

print ("apple" in fruitList)


print (max(fruitList))
print (min(fruitList))
