#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
Author: fasion
Created time: 2022-01-21 17:13:09
Last Modified by: fasion
Last Modified time: 2022-01-21 17:14:20
'''

import html


class SmartDict(dict):

    ATTR_NAMES = set()

    def __getattr__(self, name):
        if name in self.ATTR_NAMES:
            return super(SmartDict, self).__getattr__(name)

        return self[name]

    def __setattr__(self, name, value):
        if name in self.ATTR_NAMES:
            return super(SmartDict, self).__setattr__(name, value)

        self[name] = value


class HTMLAttribute(SmartDict):

    def to_html_chips(self):
        chips = []
        for k, v in self.items():
            chips.append('%s="%s"' % (k, v))
        return chips

    def to_html(self):
        return ' '.join(self.to_html_chips())


class HTMLStyle(dict):

    def to_html_chips(self):
        chips = []
        for k, v in self.items():
            chips.append('%s:%s;' % (k, v))
        return chips

    def to_html(self):
        return ''.join(self.to_html_chips())


class HTMLTag(object):

    def __init__(self, tag, value=None, value_formatter=str, escape=True):
        self.set_tag(tag=tag)
        self.set_value(value=value)
        self.set_value_formatter(formatter=value_formatter)
        self.set_escape(escape=escape)

        self.attr = HTMLAttribute()
        self.style = HTMLStyle()

    def set_tag(self, tag):
        self.tag = tag

    def set_value(self, value):
        self.value = value

    def set_value_formatter(self, formatter):
        self.value_formatter = formatter

    def set_single_style(self, name, value):
        self.style[name] = value

    def set_style(self, style):
        self.style.update(style)

    def set_escape(self, escape):
        self.escape = escape

    def to_html_inner_chips(self):
        chips = []
        if self.value:
            value = self.value_formatter(self.value)
            if self.escape:
                value = html.escape(value)

            chips.append(value)
        return chips

    def to_html_inner(self):
        return ''.join(self.to_html_inner_chips())

    def to_html_chips(self):
        chips = ['<', self.tag]

        if self.attr:
            for chip in self.attr.to_html_chips():
                chips.append(' ')
                chips.append(chip)

        if self.style:
            chips.append(' style="')
            chips.extend(self.style.to_html_chips())
            chips.append('"')

        chips.append('>')

        chips.extend(self.to_html_inner_chips())

        chips.append('</%s>' % (self.tag,))

        return chips

    def to_html(self):
        return ''.join(self.to_html_chips())
