"""Excel-to-CSV Converter."""
import os
import csv
import openpyxl


def xl_to_csv(xl_file):
    """Excel-to-CSV Converter."""
    os.chdir(os.path.dirname(xl_file) if os.path.dirname(xl_file) else '.')
    work_book = openpyxl.load_workbook(xl_file)
    for sheet in work_book.worksheets:
        output_file = f'{os.path.splitext(os.path.basename(xl_file))[0]}_{sheet.title}.csv'
        with open(output_file, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in sheet.values:
                csv_writer.writerow(row)


if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    xl_to_csv('input.xlsx')
