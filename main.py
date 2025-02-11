



def count_characters(text):
    char_count = {}
    for character in text:
        lowercase_char = character.lower()
        if lowercase_char in char_count:
            char_count[lowercase_char] += 1
        else:
            char_count[lowercase_char] = 1
    return char_count

def sort_on(dict):
    return dict["count"]

def generate_report(text):
    alphabet_chars = []
    for char, count in text.items():
        if char.isalpha():
            alphabet_chars.append({"char": char, "count": count}) 

    alphabet_chars.sort(key=sort_on, reverse=True)    


    report = " --- Begin report of Frankenstein ---"

    for char_info in alphabet_chars:
        report += f"The '{char_info['char']}' character was found {char_info['count']} times\n"

    report += "--- End report ---"
    
    return report
    


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    char_counts = count_characters(file_contents)    
    report = generate_report(char_counts)
    print(report)

main()