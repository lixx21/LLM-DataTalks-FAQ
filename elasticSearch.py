from re import S
from elasticsearch import Elasticsearch
from tqdm.auto import tqdm

def createIndex(index_name):

    es_client = Elasticsearch('http://localhost:9200') 
    #create index settings
    index_settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "properties": {
                "text": {"type": "text"},
                "section": {"type": "text"},
                "question": {"type": "text"},
                "course": {"type": "keyword"} 
            }
        }
    }

    es_client.indices.create(index=index_name, body=index_settings)

    return es_client

def elastic_search(esclient, query, index_name):
    search_query = {
        "size": 5, # number of results
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query,
                        "fields": ["question^4", "text", "section"], # question boost 4
                        "type": "best_fields"
                    }
                }
                # "filter": {
                #     "term": {
                #         "course": filter
                #     }
                # }
            }
        }
    }

    response = esclient.search(index=index_name, body=search_query)
    
    result_docs = []
    # print(response)
    for hit in response['hits']['hits']:
        # result_docs.append(hit['_source']),
        result_docs.append(hit)
    
    return result_docs