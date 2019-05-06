# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])

    return max_product


if __name__ == '__main__':
    input_n = input("Insert your numbers separated by commas: ")
    input_numbers = [int(x) for x in input_n.split()]
    print(max_pairwise_product(input_numbers))
