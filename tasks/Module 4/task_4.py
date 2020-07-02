"""Spreadsheet Cell Inventer."""
import openpyxl


def spreadsheet_cell_inverter(file_path):
    """Spreadsheet Cell Inventer."""
    source_wb = openpyxl.load_workbook(file_path)
    source_ws = source_wb.active
    rotated_rows = list(zip(*reversed(list(source_ws.values))))
    new_wb = openpyxl.Workbook()
    new_ws = new_wb.active
    for row in rotated_rows:
        new_ws.append(row)
    new_wb.save('output.xlsx')


if __name__ == '__main__':
    spreadsheet_cell_inverter('input.xlsx')
