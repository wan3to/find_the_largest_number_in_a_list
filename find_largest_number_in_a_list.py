def second_largest():
    lst = [4, 3, 1, 2]
    unique_list = list(set(lst))  # Remove duplicates
    unique_list.sort(reverse=True)
    return unique_list[1]

print(second_largest())  # Output: 3
