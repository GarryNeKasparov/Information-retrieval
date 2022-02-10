import os, json
import pandas as pd
from process_text import clean, text_to_pos, pos_with_file
from multiprocessing import Manager
from functools import partial
from scipy import spatial
from useful_functions import featured

plots_path = './MovieSummaries/MovieSummaries/plot_summaries.txt'
index_path = './done.txt'
titles = 'MovieSummaries\MovieSummaries\movie.metadata.tsv'
df = pd.read_csv(plots_path, sep='\t', header=None)
titles = pd.read_csv(titles, sep='\t', header=None)

class Document:
    def __init__(self, title, text):
        self.title = title
        self.text = text
    
    def format(self, query):
        # возвращает пару тайтл-текст, отформатированную под запрос
        return [self.title, self.text + ' ...']

def get_doc(id):
    global df
    text = df.loc[df[0] == id][1].to_string(index=False)
    title = titles.loc[titles[0] == id][2].to_string(index=False)
    return Document(title=title, text=text)

def build_index():
    def pipeline(line, file_idx):
        line = clean(line)[0].split()
        name = line[0]
        file_idx[name] = text_to_pos(line[1:])

    with open(plots_path, 'r', errors='ignore', encoding='iso8859-5') as f:
        with Manager() as mgr:
            d = mgr.dict()
            with mgr.Pool(os.cpu_count()) as pool:
                process = partial(pipeline, file_idx=d)
                pool.map(process, f.readlines())
                file_idx = pos_with_file(d)
    return file_idx
    #json.dump(file_idx, open('done.txt', 'w')) -> в дальнейшем можно просто прочитать
    

def score(query, document):
    tfidf = featured(query, document.text)
    return spatial.distance.cosine(tfidf.iloc[0], tfidf.iloc[1])

def retrieve(query, index):
    if query == '':
        return ''
    global df

    words = clean(query)[0].split()
    indexes_sets = [set(map(lambda x: int(x), index[word].keys())) for word in words if word in index.keys()]   
    if indexes_sets == []:
        return ''
    intr = indexes_sets[0]
    for idx in indexes_sets[1:]:
        intr = intr.intersection(idx)
    docs = [get_doc(x) for x in list(intr)[:10]]
    return docs


