#!/usr/bin/env python3

class ParseError(Exception):
    """ Error while parsing file """
    def __init__(self, *args, line_no: int = -1, text: str = ""):
        super().__init__(*args)
        self._args = args
        self._line_no = line_no
        self._text = text

    def __str__(self):
        if self._text == "" and self._line_no != -1:
            return f"cannot parse text on line {self._line_no}"
        if self._text != "" and self._line_no == -1:    
            return f"cannot parse text: '{self._text}'"
        if self._text != "" and self._line_no != -1:
            return f"cannot parse text on line {self._line_no}: '{self._text}'"
        else:
            return super().__str__()

raise ParseError(line_no=10, text='...')
