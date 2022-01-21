#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
Author: fasion
Created time: 2022-01-21 17:13:09
Last Modified by: fasion
Last Modified time: 2022-01-21 17:14:31
'''


class HTMLTableColumn(object):

    def __init__(self, table, index):
        self.table = table
        self.index = index

    def iter_cells(self):
        for row in self.table:
            yield row[self.index]

    def iter_data_cells(self):
        for row in self.table.iter_data_rows():
            yield row[self.index]

    def set_cell_style(self, style):
        for cell in self.iter_cells():
            cell.set_style(style=style)
