# CSE 231 – Fall 2008 – Project #5: Latin Word Parts Counter

def read_parts(filename):
   
    with open(filename, 'r') as file:
        lines = file.readlines()

    mode = None
    prefixes, roots, suffixes = {}, {}, {}

    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            if line.lower().startswith('#prefix'):
                mode = 'prefix'
            elif line.lower().startswith('#root'):
                mode = 'root'
            elif line.lower().startswith('#suffix'):
                mode = 'suffix'
            continue

        part = line.split()[0].lower()

        if mode == 'prefix':
            prefixes[part] = 0
        elif mode == 'root':
            roots[part] = 0
        elif mode == 'suffix':
            suffixes[part] = 0

    return prefixes, roots, suffixes


def count_matches(word_file, prefixes, roots, suffixes):
    """
    Counts how many words start with prefixes, contain roots, or end with suffixes.
    Updates dictionaries in-place.
    """
    with open(word_file, 'r') as f:
        for line in f:
            word = line.strip().lower()

            for pre in prefixes:
                if word.startswith(pre):
                    prefixes[pre] += 1

            for root in roots:
                if root in word:
                    roots[root] += 1

            for suf in suffixes:
                if word.endswith(suf):
                    suffixes[suf] += 1


def print_results(category, part_dict):
    """
    Outputs a formatted result for the given category.
    """
    for part in sorted(part_dict):
        count = part_dict[part]
        print("%-10s %12s %8d" % (category, part, count))


def main():
    prefix_dict, root_dict, suffix_dict = read_parts("rootsPrefixesSuffixes.txt")

    count_matches("longWordList.txt", prefix_dict, root_dict, suffix_dict)

    print("%-10s %12s %8s" % ("Category", "Part", "Count"))
    print("-" * 36)
    print_results("Prefix", prefix_dict)
    print_results("Root", root_dict)
    print_results("Suffix", suffix_dict)


if __name__ == "__main__":
    main()
