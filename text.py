import codecs
from process_text import clean, text_to_pos, pos_with_file
 
file = codecs.open('./MovieSummaries/MovieSummaries/plot_summaries.txt', 'r+', 'utf_8_sig')

lines = file.readlines()
for line in lines[0:1]:
    line = clean(line)[0].split()
    name = line[0]
    file_idx = {name : text_to_pos(line[1:])}
    file_idx = pos_with_file(file_idx)
print(file_idx)