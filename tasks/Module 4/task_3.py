"""Run Selective Copy."""
import os


def selective_copy(source_folder, destination_folder, extention):
    """Run Selective copy."""
    #os.chdir(source_folder)
    os.makedirs(destination_folder, exist_ok=True)
    with os.scandir(source_folder) as scandir:
        for entry in scandir:
            if entry.name.endswith(extention) and entry.is_file():
                print(f'Move {entry.path} to folder {destination_folder}')
                os.replace(entry.path,
                           os.path.join(destination_folder, entry.name))


if __name__ == '__main__':
    selective_copy(os.getcwd(),
                   os.path.join(os.getcwd(), 'selective_copy'), '.png')
