#pip install pyserini

#pip install faiss-cpu

import json

data = {}


corpus_path=/content/drive/MyDrive/corpus.jsonl
modified_corpus_path=/content/drive/MyDrive/TOT_Jsonl/corpus_modified.jsonl

with open(modified_corpus_path, 'w') as f1:
    with open('corpus_path', 'r') as f:
        for line in f:
            data = json.loads(line.strip())
            x = data["doc_id"]
            data["id"] = x
            x = data["text"]
            data["contents"] = x
            text = json.dumps(data)
            f1.write(text)
print("Data Converted")

!python -m pyserini.index.lucene --collection JsonCollection --input /content/drive/MyDrive/TOT_Jsonl\
 --index /content/drive/MyDrive/TOT_Jsonl_index/ --generator DefaultLuceneDocumentGenerator --threads 1 --storePositions --storeDocvectors --storeRaw
