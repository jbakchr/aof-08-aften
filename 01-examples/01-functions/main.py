"""
Eksempler på brugen af funktioner
"""


# Eksempel 1.1 - Definition a en funktion uden parametre
def my_function():
    print("Eksempel 1: This is a super function!")


# Eksempel 1.2 - Hvordan man kalder en funktion
my_function()


# Eksempel 2 - Definition af en funktion med parametre
def add_numbers(num1, num2):
    print(num1 + num2)


add_numbers(1, 5)


# Eksempel 3.1 - Funktion med enkel parameter og 'return' keyword
def greet_me(name):
    if name == "Jonas":
        return f"Whooa .. {name} is such an awesome name!"
    return f"Hi {name}!"


print(greet_me("Jonas"))
# print(greet_me("Bo"))


# Eksempler 3.2 - Funktion med flere parametre og 'return' keyword
def exponent_function(base, exponent):
    return base**exponent


print(exponent_function(8, 3))
