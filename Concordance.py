import string

def load_stop_words(filename):
    with open(filename, 'r') as f:
        stopwords = set(word.strip().lower() for word in f.readlines())
    return stopwords

def build_concordance(filename, stopwords):

    concordance = {}
    with open(filename, 'r') as f:
        lines = f.readlines()

    for line_num, line in enumerate(lines, start=1):
        original_line = line.strip()
        clean_line = original_line.translate(str.maketrans('', '', string.punctuation))
        words = clean_line.lower().split()

        for word in words:
            if word not in stopwords:
                word_upper = word.upper()
                line_highlighted = highlight_word(original_line, word)

                if word not in concordance:
                    concordance[word] = []

                concordance[word].append((line_num, line_highlighted))
    return concordance

def highlight_word(line, word):
    words = line.split()
    result = []
    for w in words:
        if w.strip(string.punctuation).lower() == word:
            result.append(w.upper())
        else:
            result.append(w)
    return ' '.join(result)

def print_concordance(concordance, filename):
    print(f"\nConcordance for file {filename}")
    for word in sorted(concordance):
        print(f"{word} : Total Count: {len(concordance[word])}")
        for line_num, context in concordance[word]:
            print(f" Line:{line_num}: {context}")
        print()

def main():
    stop_file = "english.stop.txt"
    stopwords = load_stop_words(stop_file)

    filename = input("Analyze what file: ").strip()
    try:
        concordance = build_concordance(filename, stopwords)
        print_concordance(concordance, filename)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

if __name__ == "__main__":
    main()
