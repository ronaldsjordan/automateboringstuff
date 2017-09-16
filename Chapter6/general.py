# Double Quotes
print('# Double Quotes')
spam = "That is Alice's cat."
print(spam)

# Escape Characters
print('# Escape Characters')
spam = 'Say hi to Bob\'s mother.'
print(spam)

print("Hello there!\nHow are you?\nI\'m doing fine.")

# Raw Strings
print('# Raw Strings')
print(r'That is Carol\'s cat.')

# Multiline Strings with Triple Quotes
print('# Multiline Strings with Triple Quotes')
print('# Multiline Strings with Triple Quotes')
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

# Multiline Comments
print('# Multiline Comments')
"""This is a test Python program.
Written by Al Sweigart

This program was designed for Python 3, not Python 2.
"""

def spam():
    """This is a multiline comment to help
    explain what the spam() function does."""
    print('Hello!')

# Indexing and Slicing Strings
print('# Indexing and Slicing Strings')
spam = 'Hello world!'
print(spam[0])
print(spam[4])
print(spam[-1])
print(spam[0:5])
print(spam[:5])
print(spam[6:])

# The in and not in Operators with Strings
print('# The in and not in Operators with Strings')
print('Hello' in 'Hello World')
print('Hello' in 'Hello')
print('HELLO' in 'Hello World')
print('' in 'spam')
print('cats' not in 'cats and dogs')

# The upper(), lower(), isupper(), and islower() String Methods
print('# The upper(), lower(), isupper(), and islower() String Methods')
spam = 'Hello world!'
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)

# The isX String Methods
print('# The isX String Methods')
print('hello'.isalpha())
print('hello123'.isalpha())
print('hello123'.isalnum())
print('hello'.isalnum())
print('123'.isdecimal())
print('     '.isspace())
print('This Is Title Case'.istitle())
print('This Is Title Case 123'.istitle())
print('This Is not Title Case'.istitle())
print('This Is NOT Title Case Either'.istitle())

# The startswith() and endswith() String Methods
print('# The startswith() and endswith() String Methods')
print('Hello world!'.startswith('Hello'))
print('Hello world!'.endswith('world!'))
print('abc123'.startswith('abcdef'))
print('abc123'.endswith('12'))
print('Hello world!'.startswith('Hello world!'))
print('Hello world!'.endswith('Hello world!'))

# The join() and split() String Methods
print('# The join() and split() String Methods')
print(', '.join(['cats', 'rats', 'bats']))
print(' '.join(['My', 'name', 'is', 'Simon']))
print('ABC'.join(['My', 'name', 'is', 'Simon']))
print('My name is Simon'.split())
print('MyABCnameABCisABCSimon'.split('ABC'))
print('My name is Simon'.split('m'))
spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''
print(spam.split('\n'))

# Justifying Text with rjust(), ljust(), and center()
print('# Justifying Text with rjust(), ljust(), and center()')
print('Hello'.rjust(10))
print('Hello'.rjust(20))
print('Hello World'.rjust(10))
print('Hello'.ljust(10))
print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '-'))
print('Hello'.center(20))
print('Hello'.center(20, '='))
