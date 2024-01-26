ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
N = 66

def encrypt():
    with open('data.txt','r', encoding='utf-8') as f:
        data = f.readlines()

    key = int(data[0])
    str = data[1]
    encrypted_str = ''

    for i in str:
        curr_index = ALPHABET.find(i)
        if curr_index == -1:
           encrypted_str += i
        else:
            encrypted_str += ALPHABET[(curr_index + key) % N]

    return encrypted_str

#def decrypt():

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(encrypt())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
