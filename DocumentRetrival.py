# Document Retrieval Engine

import string

def read_documents(filename):
    with open(filename, "r") as file:
        content = file.read()
        docs = content.split("<NEW DOCUMENT>")
        return [doc.strip() for doc in docs if doc.strip()]

def build_index(doc_list):
    index = {}
    for i, doc in enumerate(doc_list):
        doc_num = i + 1
        words = doc.lower().translate(str.maketrans("", "", string.punctuation)).split()
        for word in words:
            if word not in index:
                index[word] = set()
            index[word].add(doc_num)
    return index

def search_documents(index, words):
    result = None
    for word in words:
        word = word.lower().strip(string.punctuation)
        if word in index:
            if result is None:
                result = index[word].copy()
            else:
                result &= index[word]
        else:
            return set()  
    return result if result else set()

def main():
    filename = input("Enter the document file name: ")
    try:
        docs = read_documents(filename)
    except FileNotFoundError:
        print("File not found.")
        return

    index = build_index(docs)

    while True:
        print("\\nMenu:")
        print("1. Search documents")
        print("2. Display document")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            search_input = input("Enter search words: ")
            words = search_input.strip().split()
            matches = search_documents(index, words)
            if matches:
                print("Documents containing all words:", sorted(matches))
            else:
                print("No matching documents found.")

        elif choice == "2":
            try:
                doc_num = int(input("Enter document number: "))
                if 1 <= doc_num <= len(docs):
                    print(f"\\nDocument {doc_num} content:")
                    print(docs[doc_num - 1])
                else:
                    print("Invalid document number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()