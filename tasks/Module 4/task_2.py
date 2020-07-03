"""Fill in the Gaps."""
import os
MIN_ZEROES = 3


def fill_gaps(folder_path, prefix):
    """Fill in the Gaps."""
    # init file list with first not needed element
    file_list = [None]
    os.chdir(folder_path)
    # get list of tuples of filenames and extentions
    with os.scandir(folder_path) as scandir:
        file_list += sorted([os.path.splitext(entry.name) for entry in scandir
                             if entry.name.startswith(prefix) and entry.is_file()])
    # check if sequence number equal to number in filename and rename it if is not.
    number_of_zeroes = max(MIN_ZEROES, len(str(len(file_list))))
    for i, file_data in enumerate(file_list):
        if not file_data:
            continue
        file_name, file_extension = file_data
        number = int(file_name[len(prefix):])
        if i != number:
            new_file_name = prefix + str(i).zfill(number_of_zeroes) \
                            + file_extension
            os.renames(''.join(file_data), new_file_name)
            print(new_file_name)


if __name__ == '__main__':
    fill_gaps(os.path.dirname(__file__), 'spam')
