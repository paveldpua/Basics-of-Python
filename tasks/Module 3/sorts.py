"""Sort."""


def merge(A: list, B: list):
    """Merge 2 sorted lists and return result."""
    i = j = 0
    C = list()
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    C.extend(A[i:] + B[j:])
    return C


def merge_sort(A: list):
    """Merge sort."""
    # print(A)
    if len(A) <= 1:
        return A
    middle = len(A)//2
    L = A[:middle]
    R = A[middle:]
    merge_sort(L)
    merge_sort(R)
    # print(f'merge L {L} and R {R}')
    C = merge(L, R)
    A[:] = C
    # print(f'A after merge is {A}')
    return A


def hoar_sort(A: list):
    """Hoar sort."""
    # print(A)
    if len(A) <= 1:
        return A
    barrier = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        if x == barrier:
            M.append(x)
        if x > barrier:
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    A[:] = L + M + R
    return A


if __name__ == '__main__':
    a = [6, 4, 5, 7, 3, 8, 2, 3, 6, 9, 1, 9, 0, 4, 5, 6, 3, 4]
    print(merge_sort(a))
    b = [60, 40, 50, 70, 30, 80, 20, 30, 60,
         90, 10, 90, 00, 40, 50, 60, 30, 40]
    print(hoar_sort(b))
