"""
This is a file operation example.
"""

#!python3
# filename: file_op.py

import os

# Get the absolute path of the current file
current_file_path = os.path.abspath(__file__)
print(f"Current file path: {current_file_path}")

basename = os.path.basename(__file__)
dirname = os.path.dirname(__file__)


filename = "file_op.py"


def open_file(name: str):
    """Open file and print the content."""

    name = os.path.join(dirname, name)
    with open(name, mode="r", encoding="utf8") as file:
        for line in file:
            print(line, end="")

        file.close()


def write_file(name: str, content: str):
    """Write content to file."""

    name = os.path.join(dirname, name)
    with open(name, "a", encoding="utf8") as file:
        file.write(content)
        file.close()


open_file(filename)
write_file("file_demo.txt", "This is a demo file.\nThis is the second line")
