def to_ascii(string):
    return [ord(i) for i in string]


def validate_key_length(key):
    if len(key) == 0:
        raise ValueError("key cannot be empty)")


def validate_character_range(char_ascii_code):
    VALID_ASCII_RANGE = range(ord('A'), ord('Z') + 1)
    if char_ascii_code not in VALID_ASCII_RANGE:
        raise ValueError("key character is out of valid range [A-Z]")


def calculate_offset(text_ascii, key_ascii, encryption):
    """
    If encryption=True, method will calculate offset for encryption
    Else, will calculate offset for decryption
    """
    ALPHABET_LENGTH = 26
    if not encryption:
        key_ascii *= -1
    return (text_ascii + key_ascii) % ALPHABET_LENGTH


def get_nth_ascii_char(ascii_offset):
    ALPHABET_START = ord('A')
    return chr(ascii_offset + ALPHABET_START)


def get_encrypted_decrypted_text(text_ascii, key_ascii, encryption):
    key_length = len(key_ascii)

    SPACE_CHAR = ' '
    SPACE_ASCII_CODE = ord(SPACE_CHAR)

    encrypted = ''

    for i, cipher_char_ascii_code in enumerate(text_ascii):
        if cipher_char_ascii_code == SPACE_ASCII_CODE:
            encrypted += SPACE_CHAR
            continue

        validate_character_range(cipher_char_ascii_code)

        key_char_ascii_code = key_ascii[i % key_length]
        validate_character_range(key_char_ascii_code)

        offset = calculate_offset(
            cipher_char_ascii_code, key_char_ascii_code, encryption)
        encrypted += get_nth_ascii_char(offset)
    return encrypted


def get_encrypted_text(plaintext_ascii, key_ascii):
    return get_encrypted_decrypted_text(plaintext_ascii, key_ascii, encryption=True)


def get_decrypted_text(ciphertext_ascii, key_ascii):
    return get_encrypted_decrypted_text(ciphertext_ascii, key_ascii, encryption=False)


def encrypt_vigenere2(key, plaintext):
    validate_key_length(key)

    key_ascii = to_ascii(key)
    plaintext_ascii = to_ascii(plaintext)

    return get_encrypted_text(plaintext_ascii, key_ascii)


def decrypt_vigenere2(key, ciphertext):
    validate_key_length(key)

    key_ascii = to_ascii(key)
    ciphertext_ascii = to_ascii(ciphertext)

    return get_decrypted_text(ciphertext_ascii, key_ascii)
