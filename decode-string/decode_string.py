# Given a set of individual letter translations, apply them to a string from a file

# Things to consider:
# Order of lines, which lines contain translations
# How translations are defined
# Valid/invalid characters
# Empty lines
# What if there is more than one phrase to be translated?

# When using interactive python mode: decode_string("decode_string.txt")

def decode_string(file): 

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

def decode_string_refactored(file):

    translate_letters = {}
    translated_list = []
    
    for line_content in file_contents:
        if "=" in line_content:
            first, second = line_content.split("=")
            translate_letters[first] = second
            
        else: 
            for letter in line_content:
                new_phrase = []
                if letter in translate_letters:
                    new_phrase.append(translation_letters[letter])
                else: 
                    new_phrase.append(letter)            

            translated_list.append("".join(new_phrase)) 
            
    return translated_list


# def decode_things(file):