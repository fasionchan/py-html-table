#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   table.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

from .cell import (
    HTMLTableCell,
)
from .column import (
    HTMLTableColumn,
)
from .common import (
    HTMLTag,
)
from .row import (
    HTMLTableRow,
)

class HTMLTable(list, HTMLTag):

    def __init__(self, caption='', rows=()):
        list.__init__(self)
        HTMLTag.__init__(self, tag='table')

        self.caption = HTMLTag('caption')
        self.caption.set_value(value=caption)

        self.append_rows(rows=rows)

        self.colname2index = {}
        self.index2colname = {}

    def set_colname(self, index, name):
        old = self.index2colname.pop(index, None)
        if old is not None:
            self.colname2index.pop(old, None)

        self.colname2index[name] = index
        self.index2colname[index] = name

    def set_colnames(self, names):
        for index, name in enumerate(names):
            self.set_colname(index=index, name=name)

    def append_header_rows(self, rows):
        return self.append_rows(rows=rows, is_header=True)

    def append_data_rows(self, rows):
        return self.append_rows(rows=rows, is_header=False)

    def append_rows(self, rows, is_header=False):
        for row in rows:
            self.append(HTMLTableRow(
                cells=row,
                is_header=is_header,
            ))

    def iter_header_rows(self):
        for row in self:
            if row.is_header:
                yield row

    def iter_data_rows(self):
        for row in self:
            if not row.is_header:
                yield row

    def get_column(self, name):
        index = self.colname2index.get(name)
        if index is None:
            return
        return HTMLTableColumn(table=self, index=index)

    def iter_cols(self, *names):
        for name in names:
            yield self.get_column(name=name)

    def set_header_row_style(self, style):
        for row in self.iter_header_rows():
            row.set_style(style=style)

    def set_header_cell_style(self, style):
        for row in self.iter_header_rows():
            for cell in row:
                cell.set_style(style=style)

    def set_data_row_style(self, style):
        for row in self.iter_data_rows():
            row.set_style(style=style)

    def set_data_cell_style(self, style):
        for row in self.iter_data_rows():
            for cell in row:
                cell.set_style(style=style)

    def set_row_style(self, style):
        for row in self:
            row.set_style(style=style)

    def set_cell_style(self, style):
        for row in self:
            for cell in row:
                cell.set_style(style=style)

    def set_basic_style(self):
        border_style = {
            'border-color': '#000',
            'border-width': '1px',
            'border-style': 'solid',
            'border-collapse': 'collapse',
        }

        self.set_style(border_style)
        self.set_cell_style(border_style)

        header_cell_style = {
            'padding': '15px',
            'background-color': '#48a6fb',

            'color': '#fff',
            'font-size': '18px',
        }

        self.set_header_cell_style(header_cell_style)

    def mark_span(self):
        for row in self:
            for cell in row:
                cell.set_span(False)

        for i, row in enumerate(self):
            for j, cell in enumerate(row):
                for di in range(cell.attr.get('rowspan', 1)):
                    for dj in range(cell.attr.get('colspan', 1)):
                        if di == 0 and dj == 0:
                            continue

                        self[i+di][j+dj].set_span(True)

    def to_html_inner_chips(self):
        self.mark_span()

        chips = []

        if self.caption.value:
            chips.extend(self.caption.to_html_chips())

        for row in self:
            chips.extend(row.to_html_chips())

        return chips
