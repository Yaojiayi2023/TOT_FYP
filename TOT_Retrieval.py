#pip install pyserini

#pip install faiss-cpu
import json

index_path='/content/drive/MyDrive/TOT_Jsonl_index'
query_path='/content/drive/MyDrive/query.txt'
run_path='/content/drive/MyDrive/run.msmarco-passage.bm25tuned.txt'
json_query_path='/content/drive/MyDrive/query.jsonl'

import json


with open(query_path,"w") as f1:
  with open (json_query_path,"r") as f:
    for line in f:
      data=json.loads(line)
      #print(data)
      f1.write(data["id"])
      f1.write("\t")
      f1.write(data["text"])
      f1.write("\n")

f1.close()
f.close()


!python -m pyserini.search.lucene \
  --index index_path \
  --topics query_path \
  --output run_path \
  --output-format msmarco \
  --hits 1000 \
  --bm25 --k1 0.82 --b 0.68 \
  --threads 4 --batch-size 16
