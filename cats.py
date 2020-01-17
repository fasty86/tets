def read_file(path):
    """ Read file from path"""
    try:
        with open(path) as f:
            data = f.read()
    except FileNotFoundError:
        print(f'File {path} not found')
    else:
        print(data)
        for line in data.split('\n'):
            print(f'Animal name is {line}')

def file_count(name):
    try:
        with open(name) as book:
            text = book.read()
    except FileNotFoundError:
        pass
    else:
        return text

filename = input('input filename ')
# read_file(filename)
data = file_count(filename)
search = input('Enter seacrch word : ')
print(f'Occurances of word - {search} equal : {data.count(search.lower())}')
print(f'Occurances of word - {search} equal : {data.count(search)}')
