import sys


if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
else:
    print(sys.argv[1])


from stats import get_num_words, get_chars_dict, get_book_report, make_dict_list, sort_on, book_report_text_doc



# "books/frankenstein.txt"
def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    book_report = get_book_report(text)
    test_me = make_dict_list(text)
    full_report = book_report_text_doc(text)


    #print(f"Found {num_words} total words")
    #print(chars_dict)
    #print(book_report)                 
    #print(full_report)                 not needed, the full report is printed in stat.py
    
    


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

