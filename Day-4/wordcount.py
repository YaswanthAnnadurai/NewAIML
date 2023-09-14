def count_words(file_path):
    word_count = {}

    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    # Remove punctuation and convert to lowercase for better counting accuracy
                    word = word.strip('.,!?()[]{}"\'').lower()
                    if word:
                        word_count[word] = word_count.get(word, 0) + 1

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return word_count

if __name__ == "__main__":
    file_path = "apple.txt"
    word_count_result = count_words(file_path)
    print(word_count_result)