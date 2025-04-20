#!/usr/bin/python3

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
