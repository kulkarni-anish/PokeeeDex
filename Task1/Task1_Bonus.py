from collections import Counter

list = []
n = int(input("Enter the number of words: "))
for val in range(0,n):
    list.append(input("Enter a word: "))

dict=Counter(list)

print(dict)

for i in reversed(dict):
    print(i)


maxkey=print("Most repeated word:", max(dict,key=dict.get))
minkey = print("Least repeated word:", min(dict,key=dict.get))