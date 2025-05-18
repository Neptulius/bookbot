import sys


def get_book_text(book):
#Reads book text to string
    with open(book) as f:
        book_contents = f.read()
    return book_contents


from stats import get_count
from stats import char_counts
from stats import split_dict
from stats import final_output
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_str = (get_book_text(sys.argv[1]))
    count = get_count(book_str)

    char_str = char_counts(book_str)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    final_output(split_dict(char_str))
    print("============= END ===============")

main()
    


