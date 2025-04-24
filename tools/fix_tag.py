#!/usr/bin/python3

"""
This is a command line search and replace script used in this project to
fix placeholder tags. 
The script takes in three command line arguments: 
1. the file to change
2. the old tag that will be changed
3. the new tag that will be added
It will replace every instance of arg 2 with arg 3

Some example uses:
tools/fix_tag.py edition.xml "<line" "<lb"
this changes all instances of the "<line" placeholder tag in edition.xml to the
correct "<lb"

tools/fix_tag.py edition.xml "<tironianet/>" ""
this removes all instances of the unnecessary "<tironianet/>" tag and replaces them
with nothing

Important notes about usage
Since this is a script, it can be run without the python3 command, but you need to first 
give it permission to execute.
If you are in the project's root directory, run:
chmod +x tools/fix_tag.py
then you can run the script with the command:
tools/fix_tag.py [name of file to change] [old text] [replacement text]

VERY IMPORTANT: if your arguments include a tag with the '<' or '>' characters, you MUST
use quotes around the argument, or your terminal will think you are doing i/o redirection,
and the script will not work.
"""

import sys

def main():
    file = sys.argv[1]
    change_from = sys.argv[2]
    change_to = sys.argv[3]

    with open(file, 'r', encoding='utf-8-sig') as f:
        content = f.read()

    content = content.replace(change_from, change_to)


    with open(file, 'w', encoding='utf-8-sig') as f:
        f.write(content)

if __name__ == '__main__':
    main()
