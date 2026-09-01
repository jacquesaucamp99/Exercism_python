def reverse(text):
    """
        Reverses given string

        parameter: text (string)

        return: reverse_text (string)
    """
    reverse_text = ""
    char_array = list( text )

    for char in char_array:
        # prepends the char
        reverse_text = char + reverse_text

    return reverse_text