from search import retrieve, index
import json
import numpy as np
from useful_functions import *

right_answers = [
    ('lemon kid', 2231378),
    ('jewish teen school', 24225279),
    ('bad russian', 12837431),
    ('santa claus', 448735),
    ('rasist Ryan', 1749535),
    ('Kung Fu brother and sister', 4619034),
    ('only assholes', 22457596),
    ('Sandro wife', 17938594),
    ('terminator', 30327),
    ('rocky lang', 152328),
    ('Anton sheriff', 3920193),
    ('heist vega', 54173),
    ('Autobots fight space moon', 25001260),
    ('django', 31638720),
    ('Tony Montana', 267848),
    ('five strangers crypt', 1069944),
    ('Captain Jack escape', 999394),
    ('two lawyers fall in love with each other', 885308),
    ("magician's wife dies in water", 2809621),
    ('christmas son home alone', 216072),
    ('batman and joker death', 1040965),
    ('German 1939 jews', 65834),
    ('fight in the japanese garden', 301314),
    ('man of steel', 35119673),
    ('boy who wants to be a gangster', 64394),
    ('SS jews', 633052),
    ('banker escape from prison', 30625),
    ('mathematic student honored', 3569822),
    ('moscow man', 864614)]


all_ans = {}
for q in right_answers:
  print('Query: {}\nResults: {}\nTrue: {}\n'.format(q[0], retrieve(q[0], index), q[1]))
  all_ans[q[0]] = (retrieve(q[0], index), q[1])

with open('./marks.txt', 'r') as f:
    marks = json.loads(f.read())

for che in all_ans.keys():
  print(che, sorted(marks[che], reverse=True))

for che in marks.keys():
  res= np.array(marks[che])
  print(che, nDCG(res), precision(res, 10))