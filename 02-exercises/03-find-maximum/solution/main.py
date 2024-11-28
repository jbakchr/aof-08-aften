def find_max(numbers):
    if not numbers:
        return "Listen er tom!"
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


print(find_max([3, 5, 7, 2, 8]))
print(find_max([]))
