import sys
from stats import count_words, count_instance_char, sort_dict

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def main():
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    
    s = get_book_text(path)
    n = count_words(s)
    char = count_instance_char(s)
    arr = sort_dict(char)
    
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}\n----------- Word Count ----------")
    print(f"Found {n} total words\n--------- Character Count -------")

    for i in arr:
        if(i["char"].isalpha()):
            print(f"{i["char"]}: {i["num"]}")

    print("============= END ===============")


main()
