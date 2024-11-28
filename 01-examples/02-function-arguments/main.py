"""
Eksempler på brugen af funktionsargumenter
"""


# Eksempel 1 - funktion med mange argumenter
def say_hello(first_name, last_name, age, city):
    return f"Hi, my name is {first_name} {last_name} and I'm {age} years old and live in {city}"


print("Eksempel 1:", say_hello(49, "Jonas", 42, "Ballerup"), end="\n\n")


# Eksempel 2 - funktion med vilkårligt antal argumenter
nearest_family = ["Susane", "Bent", "Christian", "Milton", "Edgar"]
relatives = ["Lisbeth", "Karen", "John"]


def call_out(*args):
    for name in args:  # 'args' is a 'tuple'
        print("Eksempel 2:", name)


call_out(nearest_family)
call_out(nearest_family, relatives)


# Eksempel 3 - funktion med "keyword arguments"
def call_out_my_kids(first_child, second_child):
    print(f"\nEksempel 3:", f"My youngest kid is: {second_child}")


call_out_my_kids(second_child="Edgar", first_child="Milton")


# Example 4 - function with arbitary number of keyword arguments
def my_family(**kwargs):
    print("\nEksempel 4: My nearest family is:")
    for k, v in kwargs.items():  # 'kwargs' is a 'dict'
        print(f"{k}: {v}")


my_family(mom="Susanne", dad="Bent", brother="Christian", uncle="John")
