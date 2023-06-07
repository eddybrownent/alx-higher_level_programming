#!/usr/bin/python3
"""
this module has a funcion that
prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines
    after each of punctuation marks

    Args:
        text(str): the text to be worked on

    Raises:
        TypeError: if the text is not string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    punctuation_marks = ['.', '?', ':']
    lines = []
    current_line = ""

    for char in text:
        if char == ' ' and not current_line:
            continue

        current_line += char
        if char in punctuation_marks:
            lines.append(current_line.strip())
            lines.append('\n' * 2)
            current_line = ''

    if current_line:
        lines.append(current_line.strip())

    new_text = "".join(lines)
    print(new_text)
