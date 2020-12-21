import random

def caesar_cipher_encryptor(unencrypted_message):

    # Randomly determine the shift amount.
    shift_amount = random.randint(1, 25)

    # Encrypt the original message by right-shifting each character in alphabetical order.
    encrypted_message = ""
    for character in unencrypted_message:
        if 97 <= ord(character) and ord(character) <= 122:
            encrypted_message += chr(((ord(character) - 97 + shift_amount) % 26 + 97))
        elif 65 <= ord(character) and ord(character) <= 90:
            encrypted_message += chr(((ord(character) - 65 + shift_amount) % 26 + 65))
        else:
            encrypted_message += character

    # Return the encrypted message.
    return encrypted_message


# Prompt the input string.
# Remove all the leading and trailing whitespaces.
unencrypted_message = input("Enter the message to encrypt: ").strip()

# Call the encryptor.
encrypted_message = caesar_cipher_encryptor(unencrypted_message)
print("Encrypted message: " + encrypted_message)
