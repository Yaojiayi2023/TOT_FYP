# -*- coding: utf-8 -*-
"""TOT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-kuk-qYO4Nf7NUHiPWsM9ZIuPtky0pHf
"""

from google.colab import drive

drive.mount('/content/drive')

pip install pyserini

pip install faiss-cpu

import json

data = {}

with open('/content/drive/MyDrive/TOT_Jsonl/corpus_modified.jsonl', 'w') as f1:
    with open('/content/drive/MyDrive/corpus.jsonl', 'r') as f:
        for line in f:
            data = json.loads(line.strip())
            x = data["doc_id"]
            data["id"] = x
            x = data["text"]
            data["content"] = x
            text = json.dumps(data)
            f1.write(text)
print("data loaded")



import json
json_new_list=[]
count=0
with open('/content/drive/MyDrive/corpus.jsonl', 'r') as json_file:
    json_list = list(json_file)
    for json_str in json_list:
        result = json.loads(json_str)
        doc_id=result["doc_id"]
        result_new={}
        result_new["id"]=doc_id
        result_new["contents"]=result["text"]
        #print(result)
        json_new_list.append(result_new)
        count=count+1
        if count%50==0:
          print(count)

with open("/content/drive/MyDrive/json/corpus_new.jsonl","w") as f:
  json.dump(json_new_list, f)

with open('/content/drive/MyDrive/json/corpus_new.jsonl', 'r') as json_file:
    json_list = list(json_file)
    for json_str in json_list:
        result = json.loads(json_str)
        print(result)

!python /content/drive/MyDrive/convert_collection_to_jsonl.py --collection-path /content/drive/MyDrive/collection.tsv --output-folder /content/drive/MyDrive/Sayantan/index/

!python -m pyserini.index.lucene --collection JsonCollection --input /content/drive/MyDrive/json\
 --index /content/drive/MyDrive/index_TOT/ --generator DefaultLuceneDocumentGenerator --threads 1 --storePositions --storeDocvectors --storeRaw

!python -m pyserini.search.lucene --index /content/drive/MyDrive/index_TOT --topics /content/drive/MyDrive/query_tot.tsv --output /content/drive/MyDrive/run.sample.txt --bm25

!python /content/drive/MyDrive/convert_collection_to_jsonl.py --collection-path /content/drive/MyDrive/collection.tsv --output-folder /content/drive/MyDrive/Sayantan/index/

!python -m pyserini.search.lucene --index /content/drive/MyDrive/TOT_Jsonl --topics /content/drive/MyDrive/query_tot.tsv --output /content/drive/MyDrive/run.sample.txt --bm25

import json

data = {}

with open('/content/drive/MyDrive/TOT_Jsonl/corpus_modified.jsonl', 'w') as f1:
    with open('/content/drive/MyDrive/corpus.jsonl', 'r') as f:
        for line in f:
            data = json.loads(line.strip())
            x = data["doc_id"]
            data["id"] = x
            x = data["text"]
            data["contents"] = x
            text = json.dumps(data)
            f1.write(text)
print("data loaded")

!python -m pyserini.index.lucene --collection JsonCollection --input /content/drive/MyDrive/TOT_Jsonl\
 --index /content/drive/MyDrive/TOT_Jsonl_index/ --generator DefaultLuceneDocumentGenerator --threads 1 --storePositions --storeDocvectors --storeRaw