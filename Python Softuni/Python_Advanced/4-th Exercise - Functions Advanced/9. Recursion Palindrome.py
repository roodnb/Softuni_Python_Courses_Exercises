def palindrome(word, idk):
    if idk == len(word) // 2:
        return f"{word} is a palindrome"
    if word[idk] != word[-idk -1]:
        return f"{word} is not a palindrome"
    return palindrome(word, idk + 1)




print(palindrome("abcba", 0))
print(palindrome("peter", 0))