def recursiveRange(number):
    result = 0
    index = 0

    def add_recursive_range():
        nonlocal index
        nonlocal result
        if index > number:
            return
        result = result + index
        index = index + 1
        add_recursive_range()
    add_recursive_range()
    return result


print(recursiveRange(100))
