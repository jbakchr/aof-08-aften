def find_max(*args):
    if not args:
        return None
    return max(args)


print(find_max(1, 5, 3, 7, 2))
print(find_max())
