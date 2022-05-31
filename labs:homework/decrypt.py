def decrypt(plain_text, offset):
    decrypt_text = ""

    for i in plain_text:
        numerical_value = ord(i)
        if (i.isupper()):
            adjusted = ((numerical_value - offset - 65) % 26) + 65
            decrypt_text += chr(adjusted)
        elif numerical_value == 32:
            decrypt_text += i
        else:
            adjusted = ((numerical_value - offset - 97) % 26) + 97
            decrypt_text += chr(adjusted)

    return decrypt_text

print(decrypt("Xlmw gsyvwi mw kviex", 4))