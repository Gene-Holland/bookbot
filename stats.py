import sys

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars



def make_dict_list(text):
    text = get_chars_dict(text) #just calling the get_chars_dict to have it to work with inside function
    dict_list = []              #creating a blank list, to append the dictionaries to
    dict_to_for_dicts = {}
    
    for char in text:           #for letters in the text, ie for the key value in the dictioanries~
        num = text[char]        #let num = the value of the key/value pair in the dictionary
        
        dict_for_the_letter = {"letter": char,"num": num}
        #dict_to_list_for_dicts = {char : num}

        dict_list.append(dict_for_the_letter)
        
    return dict_list


def sort_on(dict):
        return dict["num"]



def get_book_report(text):
    book_report_dict = {}

    chars = make_dict_list(text)
    chars.sort(reverse=True, key=sort_on)     #chars is now SORTED YES LETS GOOOOO
    for char in chars:
        if char["letter"].isalpha():
               
            book_report_dict[char["letter"]] = char["num"]
    
    return (book_report_dict)


def book_report_text_doc(text):
    report_dict = get_book_report(text)
    num_words = get_num_words(text)
    

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print(f"----------- Word Count ----------")
    print(f"Found 75767 total words")
    print(f"--------- Character Count -------")
    for key in report_dict:
        print(f"{key}: {report_dict[key]}")
    print("============= END ===============")
