def main():
    book_path = "books/frankenstien.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_num_letters(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"----- Begin report of {book_path} -----")
    print(f"{num_words} words found in this document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print(f"----- End report -----")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open("books/frankenstien.txt") as f:
        return f.read()

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
        sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
def sort_on(d):
    return d["num"]
  
def get_num_letters(text):
    letter_count = {}
    for c in text:
        lowered = c.lower()
        if lowered in letter_count:
            letter_count[lowered] += 1
        else:
            letter_count[lowered] = 1
    return(letter_count)

main()