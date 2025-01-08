def main():
    book_path = "/home/toaster/workspace/github.com/IvKovalenko/bookbot/books/frankenstein.txt"
    test_string = "this is test string"
    text = get_book_text(book_path)
    #print(text)
    words = count_words(text)
    #print(count_letters(text))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print("")
    print_letters(count_letters(text))
    print("--- End report ---")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(string):
    return len(string.split())

def count_letters(string):
    dict = {}
    lowered_string = string.lower()
    splited_string = lowered_string.split()
    for word in splited_string:
        for char in word:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
    return dict

def sort_on(dict):
    return dict["count"]

def print_letters(dict):
    new_list = convert_dict_to_list(dict)
    new_list.sort(reverse=True,key=sort_on)
    for elem in new_list:
        if elem["Letter"].isalpha():
            print(f"The '{elem["Letter"]}' character was found {elem["count"]}")
    

def convert_dict_to_list(d):
    return [{"Letter": key, "count": value} for key, value in d.items()]

main()