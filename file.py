# -*- coding: UTF-8 -*-
import xlrd


# 读文件
def get_file_values(path, name):
    read = xlrd.open_workbook(path)
    table = read.sheet_by_name(name)

    mo = []
    t = []
    for i in range(table.nrows):
        mo.append(table.cell_value(i, 0))
        t.append(table.cell_value(i, 1))
    return mo, t

