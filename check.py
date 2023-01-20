import requests
import json
import elasticsearch

def search(uri, term):
    """Simple Elasticsearch Query"""
    query = json.dumps({
        "query": {
            "match": {
                "content": term
            }
        }
    })
    response = requests.get(uri, data=query)
    results = json.loads(response.text)
    print(results)
    return results

def format_results(results):
    """Print results nicely:
    doc_id) content
    """
    data = [doc for doc in results['hits']['hits']]
    for doc in data:
        print("%s) %s" % (doc['_id'], doc['_source']['content']))
#
# from elasticsearch import Elasticsearch
#
# es = Elasticsearch()
# res = es.search(index="engine_actors", doc_type="actor", body={
#   "query": {
#     "query_string": {
#                 "query": "நடிகர் "
#             }
#     print("%s) %s" % (doc['_id'], doc['_source']['content']))

if __name__ == '__main__':
    uri_search = 'http://localhost:9200/engine_actors/actor/_search'
    results = search(uri_search, "நடிகர்")
    # format_results(results)
#   }
# })
# print("%d documents found" % res['hits']['total'])
# for doc in res['hits']['hits']: