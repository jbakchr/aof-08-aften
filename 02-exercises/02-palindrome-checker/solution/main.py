def is_palindrome(text):
    text = text.replace(
        " ", ""
    ).lower()  # Fjerner mellemrum og konverterer til små bogstaver
    return text == text[::-1]


print(is_palindrome("Racecar"))  # Output: True
print(is_palindrome("Hello"))  # Output: False
