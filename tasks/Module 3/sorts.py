"""Sort."""


def merge(list_a: list, list_b: list):
    """list_merge 2 sorted lists and return result."""
    i = j = 0
    list_c = list()
    while i < len(list_a) and j < len(list_b):
        if list_a[i] <= list_b[j]:
            list_c.append(list_a[i])
            i += 1
        else:
            list_c.append(list_b[j])
            j += 1
    list_c.extend(list_a[i:] + list_b[j:])
    return list_c


def merge_sort(list_a: list):
    """list_merge sort."""
    # print(list_a)
    if len(list_a) <= 1:
        return list_a
    middle = len(list_a)//2
    list_left = list_a[:middle]
    list_right = list_a[middle:]
    merge_sort(list_left)
    merge_sort(list_right)
    # print(f'merge list_left {list_left} and list_right {list_right}')
    list_c = merge(list_left, list_right)
    list_a[:] = list_c
    # print(f'list_a after merge is {list_a}')
    return list_a


def hoar_sort(list_a: list):
    """Hoar sort."""
    # print(list_a)
    if len(list_a) <= 1:
        return list_a
    barrier = list_a[0]
    list_left = []
    list_m = []
    list_right = []
    for element in list_a:
        if element < barrier:
            list_left.append(element)
        if element == barrier:
            list_m.append(element)
        if element > barrier:
            list_right.append(element)
    hoar_sort(list_left)
    hoar_sort(list_right)
    list_a[:] = list_left + list_m + list_right
    return list_a


if __name__ == '__main__':
    a = [6, 4, 5, 7, 3, 8, 2, 3, 6, 9, 1, 9, 0, 4, 5, 6, 3, 4]
    print(merge_sort(a))
    b = [60, 40, 50, 70, 30, 80, 20, 30, 60,
         90, 10, 90, 00, 40, 50, 60, 30, 40]
    print(hoar_sort(b))
