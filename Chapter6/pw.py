#! python3
# pw.py - An insecure password locker program

PASSWORDS = {'email': 'lskjdfoleijoij340r9u048jdsfjkshd',
             'blog': 'asdlkfjolei34fj03489h0348h',
             'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('Does not exist')
