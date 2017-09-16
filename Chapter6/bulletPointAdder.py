#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

lines = text.split('\r\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\r\n'.join(lines)
pyperclip.copy(text)
