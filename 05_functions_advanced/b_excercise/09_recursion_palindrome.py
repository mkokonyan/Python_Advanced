def palindrome(word, index):
    left = index
    right = len(word) - 1 - index
    if left >= right:
        return f"{word} is a palindrome"

    left_letter = word[index]
    right_letter = word[len(word) - 1 - index]

    if not left_letter == right_letter:
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)

print(palindrome("abcba", 0))
print(palindrome("peter", 0))
