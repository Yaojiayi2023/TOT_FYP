#pip install pyserini

#pip install faiss-cpu
import json



!python -m pyserini.search.lucene \
  --index /content/drive/MyDrive/TOT_Jsonl_index \
  --topics /content/drive/MyDrive/query.txt \
  --output /content/drive/MyDrive/run.msmarco-passage.bm25tuned.txt \
  --output-format msmarco \
  --hits 1000 \
  --bm25 --k1 0.82 --b 0.68 \
  --threads 4 --batch-size 16
