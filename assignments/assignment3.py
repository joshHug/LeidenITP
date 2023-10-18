from collections import defaultdict
from pathlib import Path

"""
In this assignment, you will implement een n-gram.
This is a earlier natural language processing (NLP) model that "learns" and "predicts" words from a corpus.
Corpus is just a fancy word for a (set of) file(s) that contain text which is used to train language models.

...
"""

def parse_text_file(file):
    """
    This function should parse a text file.
    Parsing means reading a text file and converting it from one format to another.
    For this assignment, we will read the text file and extract the sentences from it into a sentence list.
    Each sentence list will contain a word list containing the words of the sentence,
    While this sounds easy there are a few things to consider:
     - No matter if a word is written with upper or lower case letters it should be then same word.
     - We are only interested in letter and not special characters
     - We need to find where a sentence ends.
     - Numbers should be ignored.
    There are many more thing to consider, but to make it a bit easier we preprocessed the text for the most part.

    For now, each line in the document contains one sentence that needs to be split into words.
    Each sentence should start with a special word "<s>" and end with "</s>".
    Also, all punctuation should be removed.
    """
    sentence_list = []
    with open(file, 'r') as f:
        for line in f:
            word_lst = ["<s>"] + line.strip()[:-1].split(" ") + ["</s>"]

        sentence_list.append(word_lst)
    return sentence_list


# Find the text file on your computer and make it operating system insensitive.
path = Path.cwd()
path = path.glob('**/text.txt').__next__()

# This should open the file read it and parse it into a 2D list with sentences and words.
parse_text_file(path)