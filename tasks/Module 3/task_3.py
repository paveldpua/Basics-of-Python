def generate_numbers(N: int, M: int, prefix=None):
    """Generate all numbers with 0 prefix in N meter system."""
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()


def gen_bin(M, prefix=''):
    """Generate all numbers for binary system."""
    if M == 0:
        print(*prefix)
        return
    for digit in '0', '1':
        gen_bin(M-1, prefix+digit)


def generate_permutations(N: int, M: int, prefix=None):
    """Generate permutations for N numbers in M positions
    with prefix."""
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for number in range(1, N+1):
        if number in prefix:
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()


if __name__ == '__main__':
    generate_numbers(4, 3)
    print()
    generate_permutations(4, 3)
