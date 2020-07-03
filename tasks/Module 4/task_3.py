"""Run Selective Copy."""
import os


def selective_copy(source_folder, destination_folder, extention):
    """Run Selective copy."""
    os.makedirs(destination_folder, exist_ok=True)
    for dirpath, _, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.endswith(extention):
                print(f'Move {os.path.join(dirpath, filename)}'
                      ' to folder {destination_folder}')
                os.replace(os.path.join(dirpath, filename),
                           os.path.join(destination_folder, filename))


if __name__ == '__main__':
    selective_copy(os.getcwd(),
                   os.path.join(os.getcwd(), 'selective_copy'), '.png')
