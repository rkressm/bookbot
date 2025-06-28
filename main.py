import sys
from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content


def main():
    print(sys.argv[0])
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    word = count_word(text)
    char_count = char_occur(text)
    dictio_list = sorting_dictionnary(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word} total words")
    print("--------- Character Count -------")
    for dictio in dictio_list:
        print(f"{dictio["char"]}: {dictio["num"]}")


main()