from flask import Flask, render_template, request
from search import score, retrieve, build_index
from time import time
from search import index_path
import json

app = Flask(__name__, template_folder='.')
with open(index_path, 'r') as f:
    index = json.loads(f.read())


@app.route('/', methods=['GET'])
def index_serv():
    start_time = time()
    query = request.args.get('query')
    if query is None:
        query = ''
    documents = retrieve(query, index)
    documents = sorted(documents, key=lambda doc: -score(query, doc))
    results = [doc.format(query)+['%.2f' % score(query, doc)] for doc in documents] 
    return render_template(
        'index.html',
        time="%.2f" % (time()-start_time),
        query=query,
        search_engine_name="Garry's Mind",
        results=results
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
