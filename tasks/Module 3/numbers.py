"""Generate numbers."""


def generate_numbers(base: int, digits: int, prefix=None):
    """Generate numbers with 0."""
    prefix = prefix or []
    if digits == 0:
        print(*prefix)
        return
    for number in range(1, base+1):
        if number in prefix:
            continue
        prefix.append(number)
        generate_numbers(base, digits-1, prefix)
        prefix.pop()


def gen_bin(digits, prefix=''):
    """Generate all numbers for binary system."""
    if digits == 0:
        print(*prefix)
        return
    for digit in '0', '1':
        gen_bin(digits-1, prefix+digit)


def generate_permutations(base: int, digits: int, prefix=None):
    """Generate permutations for base numbers in digits positions with prefix."""
    prefix = prefix or []
    if digits == 0:
        print(*prefix)
        return
    for number in range(1, base+1):
        if number in prefix:
            continue
        prefix.append(number)
        generate_permutations(base, digits-1, prefix)
        prefix.pop()


if __name__ == '__main__':
    generate_numbers(4, 3)
    print()
    generate_permutations(4, 3)
