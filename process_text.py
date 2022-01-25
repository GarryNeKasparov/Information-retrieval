from tkinter import W
from turtle import pos
import nltk
from nltk import pos_tag
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords, wordnet
import string

#nltk.download('wordnet')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('stopwords')
#nltk.download('omw-1.4')

sw_eng = set(stopwords.words('english'))

def get_wordnet_pos(treebank_tag):
    my_switch = {
        'J': wordnet.ADJ,
        'V': wordnet.VERB,
        'N': wordnet.NOUN,
        'R': wordnet.ADV,
    }
    for key, item in my_switch.items():
        if treebank_tag.startswith(key):
            return item
    return wordnet.NOUN
    
def clean(fileline):
    cleaned_text = []
    #text = fileline.translate(str.maketrans('', '', string.punctuation))
    #text = text.lower()
    #text = text.split()
    text = fileline.split()
    text = [word for word in text if not word in sw_eng]
    lemmatizer = WordNetLemmatizer()
    pos_tagged = [(word, get_wordnet_pos(tag))
                 for word, tag in pos_tag(text)]
    cleaned_text.append(' '.join([lemmatizer.lemmatize(word, tag)
                    for word, tag in pos_tagged]))
    return cleaned_text

# input : [word1, word2, ...]
# output : [word1 : [pos 1, pos2, ...], ...]
def text_to_pos(text):
    positions = {}
    for index, word in enumerate(text):
        if word in positions.keys():
            positions[word].append(index)
        else:
            positions[word] = [index]
    return positions

# input : [document1 : [word1 : [pos 1, pos2, ...], ...], ...]
# output : [word1 : [document1 : [pos1, ...], ...], ...]
def pos_with_file(posex):
    new_pos = {}
    for doc in posex.keys():
        for word in posex[doc].keys():
            if word in new_pos.keys():
                new_pos[word].append({doc : posex[doc][word]})
            else:
                new_pos[word] = {doc : posex[doc][word]}
    return new_pos