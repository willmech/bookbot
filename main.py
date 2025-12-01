import sys

text = ""

from stats import get_book_text
from stats import get_num_words 
from stats import character_count
from stats import sort_character_count



def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
        book_path = sys.argv[1]
        print(sys.argv)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        text = get_book_text(book_path)

        num_words = get_num_words(text)
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
    
        counts = character_count(text)
        sorted_counts = sort_character_count(counts)

        for item in sorted_counts:
            char = item["char"]
            num = item["num"]
            if char.isalpha():
                print(f"{char}: {num}")
        print("============= END ===============")

main()

#In order:

# 1. main() uses book_path to get text from get_book_text.
# 2. main() passes text to get_num_words to get num_words.
# 3. main() passes the same text to character_count to get counts.
#So main() is like the coordinator:
# it gets the raw data (text)
# then hands that same data to different helper functions to compute different stats.