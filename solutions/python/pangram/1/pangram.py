def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()

    for char in sentence:
        letter_index = 0
        for letter in alphabet:
            if char == letter:
                alphabet = alphabet[:letter_index] + alphabet[letter_index + 1 :]
                break
            letter_index += 1

    if len(alphabet) == 0:
        return True

    return False
                
