import random

# Algorithmic complexity: O(n log(n))


def quick_short(list, first, last):

    # chop_list = len(list) // 2
    # firts = list[:chop_list]
    # last = list[chop_list:]
    #pivot = firts[-1]
    # i = 0
    # j = 0

    if first < last:

        pivot_index = swap(list, first, last)

        quick_short(list, first, pivot_index - 1)
        quick_short(list, pivot_index + 1, last)

    return list


def swap(list, first, last):

    pivot = list[last]
    i = first

    for j in range(first, last):
        if list[j] < pivot:
            list[i], list[j] = list[j], list[i]
            i += 1
    indexp = i
    list[indexp], list[last] = list[last], list[indexp]

    return indexp


if __name__ == '__main__':
    list_size = int(input('what will be the size of your lis? '))

    list = [random.randint(0, 50) for i in range(list_size)]
    print(list)

    ordered_list = quick_short(list, 0, len(list) - 1)
    print(ordered_list)
