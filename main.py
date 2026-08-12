from stats import chars_dict_to_sorted_list, get_word_count, count_char
import sys

def get_book_text(file_path: str) -> str:
    with open(file_path, encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path: str, word_count: int, sorted_list: list[tuple[str, int]]) -> str:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")    
    print("--------- Character Count -------")
    for sort in sorted_list:
        if sort[0].isalpha():
            print(f"{sort[0]}: {sort[1]}")
    print("============= END ===============")


def main():
    if len(sys.argv) >= 2:
        book_path = sys.argv[1]
        book = get_book_text(book_path)
        word_count = get_word_count(book)
        sorted_list = chars_dict_to_sorted_list(count_char(book))
        print_report(book_path, word_count, sorted_list)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()
