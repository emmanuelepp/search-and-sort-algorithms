import random

# Algorithmic complexity: O(n)


def linear_search(list, objetive):
    hit = False

    for item in list:
        if item == objetive:
            hit = True
    return hit


if __name__ == '__main__':
    list_size = int(input('what will be the size of your lis? '))
    objetive = int(input('what number do you want to search?? '))
    list = [random.randint(0, 50) for i in range(list_size)]

    found = linear_search(list, objetive)
    print(list)
    print('The item {} {} the list'.format(
        objetive, "is in" if found else "is not in"))
