#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
Author: fasion
Created time: 2022-01-21 17:13:09
Last Modified by: fasion
Last Modified time: 2022-01-21 17:14:05
'''

from .cell import (
    HTMLTableCell,
)
from .common import (
    HTMLTag,
)


class HTMLTableRow(list, HTMLTag):

    def __init__(self, cells=(), is_header=False):
        list.__init__(self)
        HTMLTag.__init__(self, tag='tr')

        self.is_header = is_header

        self.append_cells(cells=cells)

    def append_cell(self, value):
        cell_tag = 'th' if self.is_header else 'td'
        cell = HTMLTableCell(
            tag=cell_tag,
            value=value,
        )
        self.append(cell)
        return cell

    def append_cells(self, cells):
        for cell in cells:
            self.append_cell(cell)

    def set_cell_style(self, style):
        for cell in self:
            cell.set_style(style=style)

    def to_html_inner_chips(self):
        chips = []
        for cell in self:
            chips.extend(cell.to_html_chips())
        return chips
