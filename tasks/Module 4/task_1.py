"""Mad libs."""
import os
import re

PLACEHOLDERS = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
PATTERN = re.compile(f'{"|".join(PLACEHOLDERS)}')


def mad_lib(source_file_path):
    """Repace placeholders with user inputs."""
    output_file = source_file_path + '.fixed'
    with open(source_file_path, 'r') as read_file:
        with open(output_file, 'w') as write_file:
            for line in read_file:
                matches = PATTERN.finditer(line)
                for match in matches:
                    filler = match.group(0)
                    replace = input(f'Enter an {filler.lower()}: ')
                    line = line.replace(filler, replace, 1)
                print(line)
                write_file.write(line)


if __name__ == '__main__':
    mad_lib(os.path.join(os.getcwd(), 'example.txt'))
