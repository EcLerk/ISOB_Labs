ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
N = 33
ALPHABET_EN = 'abcdefghijklmnopqrstuvwxyz'
N_EN = 26


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.readlines()

    key = data[0]
    string = data[1]
    return key, string


def encrypt_cesar(key, string):
    encrypted_str = ''

    for i in string:
        is_upper = i.isupper()
        curr_index = ALPHABET.find(i.lower())

        if curr_index == -1:
            encrypted_str += i.upper() if is_upper else i
        else:
            encrypted_str += ALPHABET[(curr_index + key) % N].upper() if is_upper else ALPHABET[(curr_index + key) % N]

    return encrypted_str


def decrypt_cesar(key, string):
    decrypted_str = ''

    for i in string:
        is_upper = i.isupper()
        curr_index = ALPHABET.find(i.lower())

        if curr_index == -1:
            decrypted_str += i.upper() if is_upper else i
        else:
            decrypted_str += ALPHABET[(curr_index - key + N) % N].upper() if is_upper else (
                ALPHABET[(curr_index - key + N) % N])

    return decrypted_str


def generate_key(key, string):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])

    return "" . join(key)


def encrypt_vigenere(key, string):
    key = generate_key(key, string)
    encrypted_str = ''

    for i in range(len(string)):
        index = ALPHABET_EN.find(string[i])
        if index == -1:
            encrypted_str += string[i]
        else:
            encrypted_str += ALPHABET_EN[(index + ALPHABET_EN.find(key[i])) % N_EN]

    return encrypted_str


def main():
    while True:
        print('Выберете действие:\n'
              '1. Зашифровать с помощью шифра Цезаря\n'
              '2. Дешифровать с помощью шифра Цезаря\n'
              '3. Зашифровать с помощью шифра Виженера\n'
              '4. Дешифровать с помощью шифра Виженера\n'
              '0. Выход\n')

        action = input()

        if action == '1':
            key, string = get_data(encryption_path)
            print(encrypt_cesar(int(key), string) + '\n')
        elif action == '2':
            key, string = get_data(decryption_path)
            print(decrypt_cesar(int(key), string) + '\n')
        elif action == '3':
            key, string = get_data(encryption_path)
            print(encrypt_vigenere(key, string) + '\n')
        elif action == '0':
            return



if __name__ == '__main__':
    encryption_path = "encryption.txt"
    decryption_path = "decryption.txt"

    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
