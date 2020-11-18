def to_ascii(string):
    return [ord(i) for i in string]


def validate_key_length(key):
    if len(key) == 0:
        raise ValueError("key cannot be empty)")


def validate_character_range(char):
    VALID_ASCII_RANGE = range(ord('A'), ord('Z') + 1)
    if char not in VALID_ASCII_RANGE:
        raise ValueError("key character is out of valid range [A-Z]")


def calculate_offset(text_ascii, key_ascii):
    ALPHABET_LENGTH = 26
    return (text_ascii + key_ascii) % ALPHABET_LENGTH


def get_encrypted_char(ascii_offset):
    ALPHABET_START = ord('A')
    return chr(ascii_offset + ALPHABET_START)


def encrypt_vigenere2(key, plaintext):
    validate_key_length(key)

    key_ascii = to_ascii(key)
    plaintext_ascii = to_ascii(plaintext)

    encrypted = ''

    SPACE_CHAR = ' '
    SPACE_ASCII_CODE = ord(SPACE_CHAR)

    key_length = len(key)
    for i, text_char_ascii_code in enumerate(plaintext_ascii):
        if text_char_ascii_code == SPACE_ASCII_CODE:
            encrypted += SPACE_CHAR
            continue

        validate_character_range(text_char_ascii_code)

        key_char_ascii_code = key_ascii[i % key_length]
        validate_character_range(key_char_ascii_code)

        offset = calculate_offset(text_char_ascii_code, key_char_ascii_code)
        encrypted += get_encrypted_char(offset)

    return encrypted


def decrypt_vigenere2(key, ciphertext):
    pass
