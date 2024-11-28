def count_vowels(text):
    vowels = "aeiouyAEIOUY"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


print(count_vowels("Hello World"))
print(count_vowels("Python"))
