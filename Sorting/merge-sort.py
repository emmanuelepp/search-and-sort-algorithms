import random

# Algorithmic complexity: O(n log(n))


def merge_sort(list):
    if len(list) > 1:
        middle = len(list) // 2
        left = list[:middle]
        right = list[middle:]

        print(left, "-" * 20, right)

        # recursive call left
        merge_sort(left)
        # recursive call ritght
        merge_sort(right)

        # iterators for sub lists
        i = 0
        j = 0

        # iterator for principal list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

        print('Left {} {} Right'.format(left,  right))
        print(list)
        print('*' * 20)

    return list


if __name__ == '__main__':
    list_size = int(input('what will be the size of your lis? '))

    list = [random.randint(0, 50) for i in range(list_size)]
    print(list)
    print('-' * 2)

    ordered_list = merge_sort(list)
    print(ordered_list)
