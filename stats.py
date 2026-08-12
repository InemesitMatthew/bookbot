def get_word_count(word: str) -> int:
    return len(word.split())


def count_char(words: str) -> dict[str, int]:
    counted: dict[str, int] = {}
    for char in words.lower():
        if char not in counted:
            counted[char] = 1
        else:
            counted[char] += 1

    return counted


def sort_on(char: tuple[str, int]) -> int:
    return char[1]

def chars_dict_to_sorted_list(char_dict: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(char_dict.items(), reverse=True, key=sort_on)
