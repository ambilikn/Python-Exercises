#To get the count of each character in a word
import operator

def count_characters(word):
    dict = {}

    print(dict)

    for i in word:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print("The count of characters in the word "+ word+" is "+ str(dict))
    # Sort Dictionary by value using itemgetter
    sorted_dict = sorted( dict.items(), key=operator.itemgetter(1), reverse=True)
    print('Sorted Dictionary: ')
    print(sorted_dict)


word = input("Enter a word")
count_characters(word)
