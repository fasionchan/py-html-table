#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
FileName:   cell.py
Author:     Fasion Chan
@contact:   fasionchan@gmail.com
@version:   $Id$

Description:

Changelog:

'''

import html

from .common import (
    HTMLStyle,
    HTMLTag,
)


class HTMLTableCell(HTMLTag):

    def __init__(self, value, tag='td', colspan=1, rowspan=1):
        super().__init__(tag=tag, value=value)

        self.__is_span = False

        self.set_colspan(span=colspan)
        self.set_rowspan(span=rowspan)

    def set_header(self):
        self.set_tag(tag='th')

    def set_colspan(self, span):
        if span == 1:
            self.attr.pop('colspan', None)
            return

        self.attr.colspan = span

    def set_rowspan(self, span):
        if span == 1:
            self.attr.pop('rowspan', None)
            return

        self.attr.rowspan = span

    def set_span(self, is_span):
        self.__is_span = is_span

    def to_html_chips(self):
        if self.__is_span:
            return []

        return super().to_html_chips()
