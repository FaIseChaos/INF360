#! python3
# contactFinder.py - find contact information for a person within the clipboard 

import pyperclip
import re

# regular expression for phone numbers
findPhoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code (1)
    (\s|-|\.)?                      # separator (2)
    (\d{3})                         # first 3 digits (3)
    (\s|-|\.)                       # separator (4)
    (\d{4})                         # last 4 digits (5)
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension (6)
    )''', re.VERBOSE)

# regular expression for email addresses
findEmailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # username
    @                               # @ symbol
    [a-zA-Z0-9.-]+                  # domain name
    (\.[a-zA-Z]{2,4})               # dot-something
    )''', re.VERBOSE)

# find matches in clipboard text
text = str(pyperclip.paste())
findPhoneRegex.findall(text)
findEmailRegex.findall(text)

# store matches in a list
matches = []
for groups in findPhoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in findEmailRegex.findall(text):
    matches.append(groups[0])

# copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print(matches)
else: 
    print('No phone numbers or email addresses found.')

# test case
'''
800-420-7240
415-863-9900
415-863-9950
info@nostarch.com
media@nostarch.com
academic@nostarch.com
info@nostarch.com
'''