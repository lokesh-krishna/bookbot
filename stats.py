# get total word count of a book
def get_word_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return len(file_contents.split())


# get count of number of times a character appears in the book
def get_character_count(filepath):
    with open(filepath) as f:
        characters = {}

        file_contents = f.read()

        for char in list(file_contents.lower()):
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1

        return characters


def sorted_character_count(characters):
    def sort_on(items):
        return items["num"]

    sorted_list = []
    for key, value in characters.items():
        one_line_dict = {}
        one_line_dict["char"] = key
        one_line_dict["num"] = value
        sorted_list.append(one_line_dict)

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
