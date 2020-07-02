"""Mad libs."""
import os
import re

TEMPLATE = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']


def mad_lib(source_file_path):
    """Repace placeholders with user inputs."""
    tmp_file = source_file_path + '.tmp'
    with open(source_file_path, 'r') as read_file:
        with open(tmp_file, 'w') as write_file:
            for line in read_file:
                pattern = re.compile(f'{"|".join(TEMPLATE)}')
                matches = pattern.finditer(line)
                for match in matches:
                    filler = match.group(0)
                    replace = input(f'Enter an {filler.lower()}: ')
                    line = line.replace(filler, replace, 1)
                print(line)
                write_file.write(line)
    os.remove(source_file_path)
    os.rename(tmp_file, source_file_path)


if __name__ == '__main__':
    mad_lib(os.path.join(os.getcwd(), 'example.txt'))
