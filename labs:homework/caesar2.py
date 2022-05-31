def encrypt(plain_text, offset):
    cipher_text = ""

    for i in plain_text:
        numerical_value = ord(i)
        if (i.isupper()):
            adjusted = ((numerical_value + offset - 65) % 26) + 65
            cipher_text += chr(adjusted)
        elif numerical_value == 32:
            continue
        else:
            adjusted = ((numerical_value + offset - 97) % 26) + 97
            cipher_text += chr(adjusted)

    return cipher_text

print(encrypt("are we human", 2))