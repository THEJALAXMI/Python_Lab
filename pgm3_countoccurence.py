s=input("Enter a sentence: ")
print(s)
wordsList=s.split() 
print(wordsList)
uniqueWords=set(wordsList)
for word in uniqueWords:
    print(f"{word} occurs {wordsList.count(word)}times")
