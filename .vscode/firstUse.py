#numers
twenty = 20
fifty = 50
sum = twenty + fifty
print(sum)

#strings
name = 'Diego'
print(name[0], sum)

#functions and for loop
array = range(0,10)
text = ''
for i in array:
    text += str(i) + ', '
print(text[:-2])

#while loop
numIterations = 3 
while(0 < numIterations):
    print(numIterations)
    numIterations-= 1

#sets
firstSet = set('abc')
secondSet = set(['abc', 'acb'])
print(firstSet, secondSet)

#if, elif, else
var1 = 1
var2 = 2
if (var1 == var2):
    print("equals")
elif (var1 != var2):
    print("diferent")
else:
    print("other")

#task: enter number
my_input = int(input("Please enter a number: "))
for var in range(0,11):
    result = var * my_input
    print(str(my_input) + ' x ' + str(var) + ' = ' + str(result))

#operation list
listExample = ["platano", "manzana"]
listExample.append('naranja')
listExample.insert(0, 'primeraFruta')
listExtend = ['frutaExtend1', 'frutaExtend2']
listExample.extend(listExtend)
print(listExample)