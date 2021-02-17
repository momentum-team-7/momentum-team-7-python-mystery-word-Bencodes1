


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    # pass
    with open(file, 'r') as txt_file:
        words_temp = txt_file.read()
        words_list = words_temp.lower()
        words_list = words_list.split()
        words_dict = {}

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for ele in words_list:
            if ele in punctuations:
                words_list = words_list.replace(ele, "")
                words_list = words_list.replace("\n", " ")

        words_list_2 = words_list.copy()

        for word in words_list:
            if word in STOP_WORDS:
                words_list_2.remove(word)
            elif word not in words_dict:
                temp_counter = words_list_2.count(word)
                words_dict[word]   = temp_counter    
                                    
        ranked_words = sorted(words_dict.items(), key = lambda kv: kv[1], reverse=True)

        # print(ranked_words)
        for key, value in ranked_words:
            if value > 2:
                asterisks = value*'*'
                print('{:>8s}{:^2s}{:^3d}{:<29s}'.format(key, " |", value, asterisks))
            elif value <= 2:
                break    


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
