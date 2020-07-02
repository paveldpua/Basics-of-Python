"""Fill in the Gaps."""
import os


def fill_gaps(folder_path, prefix):
    """Fill in the Gaps."""
    # init file list with first not needed element
    file_list = [None]
    os.chdir(folder_path)
    # get list of tuples of filenames and extentions
    with os.scandir(folder_path) as scandir:
        for entry in scandir:
            if entry.name.startswith(prefix) and entry.is_file():
                file_list.append(os.path.splitext(entry.name))
    # check if sequence number equal to number in filename and rename it if is not.
    number_of_zeroes = len(file_list[1][0]) - len(prefix)
    for i in range(1, len(file_list)):
        number = int(file_list[i][0][len(prefix):])
        if i != number:
            new_file_name = prefix + str(i).zfill(number_of_zeroes) \
                            + file_list[i][1]
            os.renames(''.join(file_list[i]), new_file_name)
            print(new_file_name)


if __name__ == '__main__':
    userprofile = os.environ.get('USERPROFILE') \
                  + r'\Documents\Basics-of-Python\tasks\Module 4'
    print('working in ' + userprofile)
    os.chdir(userprofile)
    fill_gaps(os.getcwd(), 'spam')
