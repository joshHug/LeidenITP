import nltk  # This is a major NLP library

# download corpus
nltk.download('punkt')
from nltk.corpus import abc


i = 0
sentences = []
for s in abc.sents():
    sentence = []
    apostrophe_flag = False
    for w in s:
        w2 = "".join([l for l in w.lower() if l.isalpha() or l == "."])
        if w == "'":
            apostrophe_flag = True
        elif apostrophe_flag and w == "t":
            sentence[-1] = sentence[-1][:-1]
            sentence.append("not")
        elif len(w2) > 1:
            sentence.append(w2)
    sentence = " ".join(sentence) + "."
    sentences.append(sentence)

with open("text.txt", 'w') as f:
    f.write("\n".join(sentences))
