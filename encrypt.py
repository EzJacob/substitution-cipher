import random


def main():
    text = ""
    try:
        with open('plain_text.txt', 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: Permission denied when trying to read the file.")
    except UnicodeDecodeError as e:
        print(f"Encoding error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    if text:  # Proceed only if the text was successfully read
        result = encrypt(text, generate_key())
        try:
            with open('cipher_text.txt', 'w', encoding='utf-8') as output_file:
                output_file.write(result)
            print("\nCipher text written to 'cipher_text.txt'")
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")


def generate_key():
    alphabet_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alphabet_array_shuffle = alphabet_array.copy()
    random.shuffle(alphabet_array_shuffle)
    dic_mapped_letters = {}
    for i in range(len(alphabet_array)):
        dic_mapped_letters[alphabet_array[i]] = alphabet_array_shuffle[i]
    print(dic_mapped_letters)
    return dic_mapped_letters


def encrypt(text, mapped_ch):
    cypher_result = ""
    for ch in text:
        if ch.isalpha():
            cypher_result += mapped_ch[ch.upper()]
        else:
            cypher_result += ch
    return cypher_result


if __name__ == '__main__':
    main()

