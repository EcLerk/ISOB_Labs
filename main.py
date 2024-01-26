ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
N = 33


def encrypt():
    with open('data.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()

    key = int(data[0])
    string = data[1]
    encrypted_str = ''

    for i in string:
        is_upper = i.isupper()
        curr_index = ALPHABET.find(i.lower())

        if curr_index == -1:
            encrypted_str += i.upper() if is_upper else i
        else:
            encrypted_str += ALPHABET[(curr_index + key) % N].upper() if is_upper else ALPHABET[(curr_index + key) % N]

    return encrypted_str


def decrypt():
    

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(encrypt())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
