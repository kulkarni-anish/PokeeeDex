
list = []
newlist = []
n = int(input("Enter the number of words: "))
for val in range(0,n):
    list.append(input("Enter a word: "))
    if val not in newlist:
        newlist.append(val)

print(len(newlist))

for a in newlist:
    print(list.count(a),end=' ')
