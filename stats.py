def words_count(content):
    return len(content.split())
def character_count(content):
    counts = {}

    for char in content.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts
