from elasticsearch import Elasticsearch
import logging

logger = logging.getLogger(__name__)
GLOBAL_INDEX = 'metaphor1'
client = Elasticsearch(HOST="http://localhost", PORT=9200)


def fundamental(query):
    q = {
        "query": {
            "query_string": {
                "query": query
            }
        }
    }
    return q

def search(query):
    query_body = fundamental(query)
    logger.info("Basic search happening")
    res = client.search(index=GLOBAL_INDEX, body=query_body)
    return res

def matched_search(fields):

    query = {
        "query":{
            "bool":{
                "must":[]
            }
        }
    }
    
    for field in fields:
        query["query"]["bool"]["must"].append({"match":{field:fields[field]}})


    res = client.search(index=GLOBAL_INDEX, body=query)
    return res


def wildcard_search(query):
    q = {
       "query": {
            "wildcard": {
            "Metaphor": {
                "value": "*"+query+"*"
            }
            }
        }
    }
    res = client.search(index=GLOBAL_INDEX, body=q)

    return res