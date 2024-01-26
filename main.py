ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
N = 33


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.readlines()

    key = int(data[0])
    string = data[1]
    return key, string


def encrypt(key, string):
    encrypted_str = ''

    for i in string:
        is_upper = i.isupper()
        curr_index = ALPHABET.find(i.lower())

        if curr_index == -1:
            encrypted_str += i.upper() if is_upper else i
        else:
            encrypted_str += ALPHABET[(curr_index + key) % N].upper() if is_upper else ALPHABET[(curr_index + key) % N]

    return encrypted_str


def decrypt(key, string):
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
            print(encrypt(key, string) + '\n')
        elif action == '2':
            key, string = get_data(decryption_path)
            print(decrypt(key, string) + '\n')
        elif action == '0':
            return

    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    encryption_path = "encryption.txt"
    decryption_path = "decryption.txt"

    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
