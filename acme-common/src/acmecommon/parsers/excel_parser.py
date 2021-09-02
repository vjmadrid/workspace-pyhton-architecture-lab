# -*- coding: utf-8 -*-

import os
import xlrd


class ExcelParser:

    def __init__(self, root_dir, excel_path):
        self.excel_path = os.path.join(root_dir, excel_path)

    def read_from_excel(self, sheet_name):
        rows_val = []
        work_book = xlrd.open_workbook(self.excel_path)
        sheet = work_book.sheet_by_name(sheet_name)

        num_cols = sheet.ncols
        for row_idx in range(1, sheet.nrows):
            for col_idx in range(0, num_cols):
                cell_obj = sheet.cell(row_idx, col_idx)
                # Convert cell to string,split it according to "'" and take the second cell in the array created
                # e.g.: cell_obj == "text:'something'" --> after convert and splitting == "something"
                rows_val.append(str(cell_obj).split("'")[1])
        return rows_val
