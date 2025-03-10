
word = input("Enter a word: ")  
result = ""  
    
for i in range(len(word)):
    if i == 0 or word[i] != word[i - 1]:
        result += word[i]
    
print(result) 