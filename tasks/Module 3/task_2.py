"""My split function."""


def my_split(source_string, separator=None):
    """My implementation of split() function."""
    if separator is None:
        separator = ' '
    result = []
    if len(source_string) < len(separator):
        result.append(source_string)
        print(result)
        return result
    while len(source_string) >= 0:
        if source_string == separator:
            result.extend(['', ''])
            break
        i = source_string.find(separator)
        if i == -1:
            result.append(source_string)
            print(result)
            return result
        result.append(source_string[:i])
        source_string = source_string[i + len(separator):]
    print(result)
    return result


if __name__ == '__main__':
    my_split("Python is cool")
    my_split(",,,,", ',')
    my_split("Python", "Javascript")
    my_split('my brother broght brokoli bro', 'bro')
