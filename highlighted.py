import csv
import sys


once = 1
print('%%tana%%')

with open(sys.argv[1]) as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)

    for row in reader:
        highlight, title, author, isbn, location, tags, note, date = row
        if once == 1:
            print(f'- {title} #book')
            print(f'  - Author:: {author}')
            print(f'  - ISBN:: {isbn}')
            once = None
        print(f'- {highlight} #highlight')
        print(f'  - Book:: {title} #book')
        print(f'  - Page:: {location}')
        print(f'  - Tags:: {tags}')
        print(f'  - Notes:: {note}')
