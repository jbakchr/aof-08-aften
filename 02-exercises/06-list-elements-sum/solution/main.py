def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(sum_list([1, 2, 3, 4]))
print(sum_list([]))
