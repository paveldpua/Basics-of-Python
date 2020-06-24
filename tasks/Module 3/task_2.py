"""My split function."""


def my_split(source_string, separator=None):
    """My implementation of split() function."""
    if separator == '':
        raise ValueError('Please provide a valid separator.'
                         'It can not be an empty string')
    if separator is None:
        separator = ' '
    result = []
    if len(source_string) < len(separator):
        return [source_string]
    while len(source_string) >= 0:
        if source_string == separator:
            result.extend(['', ''])
            break
        i = source_string.find(separator)
        if i == -1:
            result.append(source_string)
            return result
        result.append(source_string[:i])
        source_string = source_string[i + len(separator):]
    return result
