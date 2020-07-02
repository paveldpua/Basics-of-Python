"""Find Mistakes in a Spreadsheet."""
import ezsheets


def find_mistakes(spreadsheet_id):
    """Find Mistakes in a Spreadsheet."""
    spreadsheet = ezsheets.Spreadsheet(spreadsheet_id)
    row = 2
    while spreadsheet[0].getRow(row)[0]:
        if int(spreadsheet[0].getRow(row)[0]) * int(spreadsheet[0].getRow(row)[1]) \
                != int(spreadsheet[0].getRow(row)[2]):
            print(f'Row {row} has mistake')
        row += 1


if __name__ == '__main__':
    find_mistakes('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
