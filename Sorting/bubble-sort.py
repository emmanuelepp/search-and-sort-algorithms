import random

# Algorithmic complexity: O(n**2)


def bubble_short(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


if __name__ == '__main__':
    list_size = int(input('what will be the size of your lis? '))

    list = [random.randint(0, 50) for i in range(list_size)]
    print(list)

    ordered_list = bubble_short(list)
    print(ordered_list)
