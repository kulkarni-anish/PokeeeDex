
list = []
newlist = []
n = int(input("Enter the number of words: "))
for val in range(0,n):
    list.append(input("Enter a word: "))
    if list[val] not in newlist:
        newlist.append(list[val])

print(len(newlist))

for word in newlist:
    print(list.count(word),end=' ')



#Alternate
#from collections import Counter
#dict=Counter(list)
#print(dict)
#for i in dict:
#    print(dict[i],end=" ")