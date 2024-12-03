"""
Recap fra 7. aften
"""

# Eksempel 1 - range loop
for i in range(1, 11, 4):
    print(f"Eksempel 1: Num is: {i}")


# Eksempel 2 - for loops
fruits = ["apple", "banana", "cherry", "grapes", "oranges"]

for fruit in fruits:
    if fruit == "banana":
        continue
    elif fruit == "grapes":
        break
    print(f"Eksempel 2: {fruit}")
else:
    print("Eksempel 2: 'Else' eksekveres hvis loop'et ikke 'breakes' ..")


# Eksempel 3 - while loops
num = 1
while num <= 10:
    if num == 3:
        num += 1
        continue
    elif num == 7:
        break
    print(f"Eksempel 3: {num}")
    num += 1
else:
    print("Eksempel 3: 'Else' eksekveres hvis loop'et ikke 'breakes' ..")
