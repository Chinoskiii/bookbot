from stats import get_num_words
from stats import count_characters
from stats import sorted_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    title = sys.argv[1]
    text = get_book_text(title)
    num_words = get_num_words(text)
    character_count = count_characters(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {title}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_chars = sorted_list(character_count)

    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    

    print("============= END ===============")
    
    
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

main()
