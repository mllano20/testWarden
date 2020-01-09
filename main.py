import datetime

from flask import Flask, render_template, jsonify, request
from google.cloud import datastore

app = Flask(__name__)




@app.route('/')
def root():

    return render_template('index.html')

@app.route('/entries', methods=['GET'])
def get_all_entries():
    client = datastore.Client()
    query = client.query()
    output = []
    fetch = query.fetch()
    results = list(fetch)    
    return jsonify({'result': results})

@app.route('/push', methods=['POST'])
def add_message():
    client = datastore.Client()
    key = client.key('Messages')
    entity = datastore.Entity(key=key)
    data = request.json

    for d in data.keys():
        
        entity.update({
            d: data[d]})
    client.put(entity)
    output = list(data.keys())
    return jsonify({'message': data,
                    'result':'Message Stored'})


if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=8080, debug=True)
