#!/usr/bin/python3
"""text_indentation module"""


def text_indentation(text):
    """text_indentation"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = text[:]
    for special_character in ".?:":
        new_list = new_text.split(special_character)
        new_text = ""
        for i in new_list:
            i = i.strip(" ")
            if new_text == "":
                new_text = i + special_character
            else:
                new_text = new_text + "\n\n" + i + special_character
    print(new_text[:-3], end="")
