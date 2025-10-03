from stats import get_count,count_alphabets,char_count_report,get_num
import sys


print(sys.argv)

def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()  # returns a list of lines


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    lines = get_book_text(book_path)
    num_word=get_count(lines)
    print(f"Found {num_word} total words")
    alphabet_count=count_alphabets(lines)
    sorted_count=char_count_report(alphabet_count)
    for item in sorted_count:
        print(f"{item['char']}: {item['num']}")
    
main()