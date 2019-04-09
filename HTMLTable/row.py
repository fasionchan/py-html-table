#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   row.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

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

    def append_cells(self, cells):
        cell_tag = 'th' if self.is_header else 'td'
        for cell in cells:
            self.append(HTMLTableCell(
                tag=cell_tag,
                value=cell,
            ))

    def set_cell_style(self, style):
        for cell in self:
            cell.set_style(style=style)

    def to_html_inner_chips(self):
        chips = []
        for cell in self:
            chips.extend(cell.to_html_chips())
        return chips
