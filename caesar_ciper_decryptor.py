import enchant

def caesar_cipher_decryptor(encrypted_message):

    # Create a dictionary of English words.
    english_word_dictionary = enchant.Dict("en_US")

    # Try all possible shift amounts to find the most possible decrypted message.
    most_possible_answer, highest_confidence = "", 0
    shift_amount = 0
    while shift_amount <= 25:

        # Attempt to decrypt with current shift amount.
        # Record all words while constructing the decrypted message.
        decrypted_message = ""
        words_in_message, word = [], ""
        for character in encrypted_message:
            if 97 <= ord(character) and ord(character) <= 122:
                decrypted_message += chr(((ord(character) - 97 - shift_amount + 26) % 26 + 97))
                word += chr(((ord(character) - 97 - shift_amount + 26) % 26 + 97))
            elif 65 <= ord(character) and ord(character) <= 90:
                decrypted_message += chr(((ord(character) - 65 - shift_amount + 26) % 26 + 65))
                word += chr(((ord(character) - 65 - shift_amount + 26) % 26 + 65))
            else:
                decrypted_message += character
                words_in_message.append(word)
                word = ""
        words_in_message.append(word)

        # Compute the self-defined confidence that the decrypted message is in English.
        num_of_english_words, num_of_words = 0, 0
        for word in words_in_message:
            if word == "":
                continue
            elif english_word_dictionary.check(word):
                num_of_words += 1
                num_of_english_words += 1
            else:
                num_of_words += 1
        
        # Update the most possible answer if the confidence of newly decrypyed message is higher.
        confidence = num_of_english_words / num_of_words
        if confidence >= highest_confidence:
            most_possible_answer = decrypted_message
            highest_confidence = confidence

        # Increment the shift amount.
        shift_amount += 1

    # Return the most possible answer and the confidence.
    return most_possible_answer, highest_confidence

# Prompt the input string.
# Remove all the leading and trailing whitespaces.
encrypted_message = input("Enter the message to decrypt: ").strip()

# Call the decryptor.
decrypted_message, confidence = caesar_cipher_decryptor(encrypted_message)
print("The most possible decrypted message: " + decrypted_message)
print("The confidence for this decrypted result: {}".format(confidence))
