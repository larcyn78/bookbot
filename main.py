import sys
from stats import (
    count_words_in_book,
    get_chars_dict,
    chars_dict_to_sorted_list
)

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        bookPath = sys.argv[1]
        text = get_book_text(bookPath)
        wordCount = count_words_in_book(text)
        letterCount = get_chars_dict(text)
        sortedList = chars_dict_to_sorted_list(letterCount)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {bookPath}")
        print("----------- Word Count ----------")
        print(f"Found {wordCount} total words")
        print("--------- Character Count -------")
        for dict in sortedList:
            if not dict["char"].isalpha():
                continue
            myChar = dict["char"]
            num = dict["num"]
            print(f"{myChar}: {num}")
        



main()
    
