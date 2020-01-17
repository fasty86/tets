import json

filename = 'user_number.json'


def get_num():
    """ask user input his favourite number """
    num = input('Please enter your favourite number : ')
    return num


def store_data(num, user='Igor'):
    line = {user: num}
    try:
        with open(filename, 'w') as f:
            json.dump(line, f)
    except FileNotFoundError:
        print(f'File not found ')
    else:
        print(f'your favourite number recorded')


def get_number(user='Igor'):
    data = ''
    try:
        with open(filename) as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f'File not found')
    else:
        try:
            print(f'{user} your favourite number is {data[user]}')
        except KeyError:
            print(f"There no record for user {user}")
        else:
            pass

def get_user():
    uname = input("Tell us your name please ")
    return uname

number = get_num()
store_data(number)
get_number(get_user())
