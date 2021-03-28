# In order to implement a binary search our data has to be sorted first.
# Algorithmic complexity: O(log n)
import random

# Complexity: O(N)


def binary_search(list, start_index, end_index, objetive):

    if start_index > end_index:
        return False

    middle = (start_index + end_index) // 2

    if list[middle] == objetive:
        return True
    elif list[middle] < objetive:
        return binary_search(list, middle + 1, end_index, objetive)
    else:
        return binary_search(list, start_index, middle - 1, objetive)


if __name__ == '__main__':
    list_size = int(input('what will be the size of your lis? '))
    objetive = int(input('what number do you want to search?? '))
    list = sorted([random.randint(0, 50) for i in range(list_size)])

    found = binary_search(list, 0, len(list), objetive)
    print(list)
    print('The item {} {} the list'.format(
        objetive, "is in" if found else "is not in"))
