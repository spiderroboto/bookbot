from stats import words_count, character_count

with open("books/frankenstein.txt", "r") as f:
    content = f.read()

total = words_count(content)
print(f"Found {total} total words")

char_counts = character_count(content)
print(char_counts)
