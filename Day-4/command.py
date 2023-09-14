import sys
from wordcount import count_words

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python command.py <file_path>")
    else:
        file_path = sys.argv[1]
        word_count_result = count_words(file_path)

        for word, count in word_count_result.items():
            print(f"{word}: {count}")