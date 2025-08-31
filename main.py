import sys
from stats import get_word_count
from stats import get_character_count
from stats import sorted_character_count


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    else:
        num_words = get_word_count(sys.argv[1])
        characters = get_character_count(sys.argv[1])
        sorted_list = sorted_character_count(characters)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in sorted_list:
            print(f"{item["char"]}: {item["num"]}")


main()
