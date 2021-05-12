word = input("Enter a word")
Dict = {}

print(Dict)

for i in word:
    if i in Dict:
        Dict[i] += 1
    else:
        Dict[i] = 1

print("The count of characters in the word "+ word+"is "+ str(Dict))
