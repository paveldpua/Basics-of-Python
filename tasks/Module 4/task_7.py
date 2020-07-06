"""Excel-to-CSV Converter."""
import os
import csv
import openpyxl


def xlsx_to_csv(xlsx_file):
    """Convert Excel worksheet to CSV files by writing each sheet into separate CSV file."""
    work_book = openpyxl.load_workbook(xlsx_file)
    for sheet in work_book.worksheets:
        output_filename = f'{os.path.splitext(os.path.basename(xlsx_file))[0]}_{sheet.title}.csv'
        output_filepath = os.path.join(os.path.dirname(xlsx_file)
                                       if os.path.dirname(xlsx_file) else '.',
                                       output_filename)
        with open(output_filepath, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in sheet.values:
                csv_writer.writerow(row)


if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    xlsx_to_csv('input.xlsx')
