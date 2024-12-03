def greet(name="Guest", greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"


print(greet())
print(greet(name="Alice"))
print(greet(greeting="Hi", name="Bob", punctuation="?"))
