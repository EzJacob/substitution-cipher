def main():
    text = ""
    try:
        with open('cipher_text.txt', 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: Permission denied when trying to read the file.")
    except UnicodeDecodeError as e:
        print(f"Encoding error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    if text:
        mapped_ch = mapped_letters(text, letter_count(text))
        result = decrypt(text, mapped_ch)
        try:
            with open('decrypted_text.txt', 'w', encoding='utf-8') as output_file:
                output_file.write(result)
            print("\nDecrypted text written to 'decrypted_text.txt'")
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")


def letter_count(text):
    letter_dic_freq = {}
    for ch in text:
        if ch in letter_dic_freq:
            letter_dic_freq[ch] += 1
        elif ch.isalpha():
            letter_dic_freq[ch] = 1
    sorted_dict = dict(sorted(letter_dic_freq.items(), key=lambda item: item[1], reverse=True))
    print("Counting the number of a character in a cipher text:")
    print(sorted_dict)
    return letter_dic_freq


def mapped_letters(text, letter_dic_freq):
    most_common_ch = {
        'e': 1, 't': 2, 'a': 3, 'o': 4, 'i': 5, 'n': 6, 's': 7, 'h': 8, 'r': 9,
        'd': 10, 'l': 11, 'c': 12, 'u': 13, 'm': 14, 'w': 15, 'f': 16, 'g': 17,
        'y': 18, 'p': 19, 'b': 20, 'v': 21, 'k': 22, 'j': 23, 'x': 24, 'q': 25, 'z': 26
    }
    most_common_ch = list(most_common_ch.keys())
    letter_dic_freq_sorted = sorted_by_values_desc = dict(
        sorted(letter_dic_freq.items(), key=lambda item: item[1], reverse=True))
    result_dic = {}
    i = 0
    for ch in letter_dic_freq_sorted:
        result_dic[ch] = most_common_ch[i]
        i += 1
    print("\nMapped characters [Cipher test character] --> [Plain text character]:")
    print(result_dic)
    return result_dic


def decrypt(text, mapped_ch):
    result = ""
    for ch in text:
        if ch.isalpha():
            result += mapped_ch[ch]
        else:
            result += ch
    return result


if __name__ == '__main__':
    main()
