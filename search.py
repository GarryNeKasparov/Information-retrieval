import random

class Document:
    def __init__(self, title, text):
        # можете здесь какие-нибудь свои поля подобавлять
        self.title = title
        self.text = text
    
    def format(self, query):
        # возвращает пару тайтл-текст, отформатированную под запрос
        return [self.title, self.text + ' ...']

index = []

def build_index():

    
    # считывает сырые данные и строит индекс
    

def score(query, document):
    # возвращает какой-то скор для пары запрос-документ
    # больше -- релевантнее
    return random.random()

def retrieve(query):
    # возвращает начальный список релевантных документов
    # (желательно, не бесконечный)
    candidates = []
    for doc in index:
        if query.lower() in doc.title.lower() or query in doc.text.lower():
            candidates.append(doc)
    return candidates[:50]
