def generate_numbers(N: int, M: int, prefix=None):
    '''generate numbers with 0'''
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for number in range(1, N+1):
        if number in prefix:
            continue
        prefix.append(number)
        generate_numbers(N, M-1, prefix)
        prefix.pop()
