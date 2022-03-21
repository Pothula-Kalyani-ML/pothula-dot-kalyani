def Caesar_encryption(text_str, shift):
    result = ""
    for character in text_str:
        if character.isupper():
            character_index = ord(character) - ord("A")
            new_char_index = (character_index + shift) % 26
            new_ascii = new_char_index + ord("A")
            new_character = chr(new_ascii)
            result = result + new_character
        elif character.islower():
            character_index = ord(character) - ord("a")
            new_char_index = (character_index + shift) % 26
            new_ascii = new_char_index + ord("a")
            new_character = chr(new_ascii)
            result = result + new_character
        else:
            result = result+character
    return result


if __name__ == "__main__":
    text_str_list = ["maple labs", "MAPLE LABS","maPle Labs"]
    shift_value = 10
    for text_str in text_str_list:
        encrypted_str = Caesar_encryption(text_str, shift_value)
        print(encrypted_str)
