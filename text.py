from process_text import clean, text_to_pos, pos_with_file
from multiprocessing import Pool, Manager
from functools import partial
import json, os
import time
from pprint import pprint


plots_path = './MovieSummaries/MovieSummaries/plot_summaries.txt'
def pipeline(line, file_idx):
    line = clean(line)[0].split()
    name = line[0]
    file_idx[name] = text_to_pos(line[1:])

if __name__ == '__main__':
    with open(plots_path, 'r', errors='ignore', encoding='iso8859-5') as f:
        with Manager() as mgr:
            d = mgr.dict()
            with mgr.Pool(os.cpu_count()) as pool:
                process = partial(pipeline, file_idx=d)
                pool.map(process, f.readlines())
                file_idx = pos_with_file(d)
        json.dump(file_idx, open('done.txt', 'w'))