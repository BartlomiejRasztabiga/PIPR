def to_ascii(string):
    return [ord(i) for i in string]


def validate_key_length(key):
    if len(key) == 0:
        raise ValueError("key cannot be empty)")


def validate_character_range(char_ascii_code):
    VALID_ASCII_RANGE = range(ord('A'), ord('Z') + 1)
    if char_ascii_code not in VALID_ASCII_RANGE:
        raise ValueError("key character is out of valid range [A-Z]")


def calculate_encryption_offset(text_ascii, key_ascii):
    ALPHABET_LENGTH = 26
    return (text_ascii + key_ascii) % ALPHABET_LENGTH


def calculate_decryption_offset(text_ascii, key_ascii):
    ALPHABET_LENGTH = 26
    return (text_ascii - key_ascii) % ALPHABET_LENGTH


def get_nth_ascii_char(ascii_offset):
    ALPHABET_START = ord('A')
    return chr(ascii_offset + ALPHABET_START)


def get_encrypted_text(plaintext_ascii, key_ascii):
    key_length = len(key_ascii)

    SPACE_CHAR = ' '
    SPACE_ASCII_CODE = ord(SPACE_CHAR)

    encrypted = ''

    for i, cipher_char_ascii_code in enumerate(plaintext_ascii):
        if cipher_char_ascii_code == SPACE_ASCII_CODE:
            encrypted += SPACE_CHAR
            continue

        validate_character_range(cipher_char_ascii_code)

        key_char_ascii_code = key_ascii[i % key_length]
        validate_character_range(key_char_ascii_code)

        offset = calculate_encryption_offset(
            cipher_char_ascii_code, key_char_ascii_code)
        encrypted += get_nth_ascii_char(offset)
    return encrypted


def encrypt_vigenere2(key, plaintext):
    validate_key_length(key)

    key_ascii = to_ascii(key)
    plaintext_ascii = to_ascii(plaintext)

    return get_encrypted_text(plaintext_ascii, key_ascii)


def get_decrypted_text(ciphertext_ascii, key_ascii):
    key_length = len(key_ascii)

    SPACE_CHAR = ' '
    SPACE_ASCII_CODE = ord(SPACE_CHAR)

    decrypted = ''

    for i, cipher_char_ascii_code in enumerate(ciphertext_ascii):
        if cipher_char_ascii_code == SPACE_ASCII_CODE:
            decrypted += SPACE_CHAR
            continue

        validate_character_range(cipher_char_ascii_code)

        key_char_ascii_code = key_ascii[i % key_length]
        validate_character_range(key_char_ascii_code)

        offset = calculate_decryption_offset(
            cipher_char_ascii_code, key_char_ascii_code)
        decrypted += get_nth_ascii_char(offset)
    return decrypted


def decrypt_vigenere2(key, ciphertext):
    validate_key_length(key)

    key_ascii = to_ascii(key)
    ciphertext_ascii = to_ascii(ciphertext)

    return get_decrypted_text(ciphertext_ascii, key_ascii)
