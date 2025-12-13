import sys
from stats import words_count, character_count

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

with open(book_path, "r") as f:
    content = f.read()

total_words = words_count(content)
char_counts = character_count(content)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print(f"Found {total_words} total words")
print("--------- Character Count -------")

sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

for char, count in sorted_chars:
    if char.isalpha():
        print(f"{char}: {count}")

print("============= END ===============")
