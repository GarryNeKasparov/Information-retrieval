from sklearn.feature_extraction.text import TfidfVectorizer
from process_text import clean
from scipy import spatial
import numpy as np
import pandas as pd

plots_path = './MovieSummaries/MovieSummaries/plot_summaries.txt'

def DCG(results):
    ix = np.arange(2, len(results) + 2)
    return np.sum(results / np.log2(ix))


def nDCG(results):
    return DCG(results) / DCG(sorted(results, reverse=True))


def precision(results, k):
    # будем считать, что если оценка > 3, то мы попали
    results = sorted(results)[:k]
    return (results.count(4) + results.count(5)) / len(results)

def featured(query, document):
    vectorizer = TfidfVectorizer()
    corpus = [clean(document)[0], clean(query)[0]]
    X = vectorizer.fit_transform(corpus).todense()
    return pd.DataFrame(X, columns=vectorizer.get_feature_names_out())


