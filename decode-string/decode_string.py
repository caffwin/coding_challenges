# Given a set of individual letter translations, apply them to a string from a file

# Things to consider:
# Order of lines, which lines contain translations
# How translations are defined
# Valid/invalid characters
# Empty lines
# What if there is more than one phrase to be translated?

# decode_list = []
# translate_this_phrase = ""
# translate_dict = {}
# new_phrase = []

# When using interactive python mode: decode_string("decode_string.txt")

def decode_string(file): 
    decode_list = []
    translate_this_phrase = ""
    translate_dict = {}
    new_phrase = []


    for row in open(file):
        stripped_row = row.rstrip("\n")

        if "=" in stripped_row:
            translate_letter, translate_to = stripped_row.split("=")
            translate_dict[translate_letter] = translate_to

        else:
            translate_this_phrase = stripped_row

    for letter in translate_this_phrase:
        if letter in translate_dict:
            new_phrase.append(translate_dict[letter])
        else: 
            new_phrase.append(letter)

        new_string = "".join(new_phrase)

    return new_string
