import re

def remove_english_characters_and_concatenate(file_path):
    concatenated_text = ""
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            cleaned_line = re.sub(r'[A-Za-z0-9_!#%*()?/;:©,.'']', '', line)
            concatenated_text += cleaned_line
    return concatenated_text

if __name__ == "__main__":
    file_path = 'News Article 6.txt'
    result = remove_english_characters_and_concatenate(file_path)
    print("Concatenated text without English alphabets:")
    print(result)