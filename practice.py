print("hello")
def addTwo(n1, n2):
    answer = n1+n2
    return answer #dont use print (answer)

print(addTwo(10,20)*2)

def addList(ls):
    #given a list of number , returns a new list with its elements adding 1
    #eg addList[10,20 returns [11,21]]
    newls =[]
    for n in ls:
        newls.append(n+1)
    return newls

print(addList([10,20,30]))

y=[11,23,34,56,67]
print(addList(y))

for a in range (-5,6):
    for b in range (-5,6):
        print(a, b)