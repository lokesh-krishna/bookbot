def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = word_counter(text)
    character_dictionary = character_counter(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words were found in the document")

    for i in character_dictionary:
        print(f"The {i} character was found {character_dictionary[i]} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_counter(text):
    split_up = str.split(text)
    return len(split_up)

def character_counter(text):
    lowercase = str.lower(text)

    character_dictionary = {}

    for l in lowercase:
        if l in character_dictionary:
            character_dictionary[l] += 1
        else:
            character_dictionary[l] = 1

    return character_dictionary

main()
