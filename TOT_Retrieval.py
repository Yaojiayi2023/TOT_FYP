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



import json
corpus_path='/content/drive/MyDrive/corpus.jsonl'
modified_corpus_path='/content/drive/MyDrive/corpus_modified.jsonl'

count=0
with open(modified_corpus_path, 'w') as f1:
    with open(corpus_path, 'r') as f:
        for line in f:
            data = json.loads(line.strip())
            x = data["doc_id"]
            data["id"] = x
            x = data["text"]
            data["contents"] = x
            text = json.dumps(data)
            f1.write(text)
            f1.write("\n")

f1.close()
print("Data Converted")

!python -m pyserini.encode input   --corpus /content/drive/MyDrive/corpus_modified.jsonl --fields text  --delimiter "\n" --shard-id 0 --shard-num 1 output  --embeddings /content/drive/MyDrive/Run/ --to-faiss encoder --encoder  castorini/tct_colbert-v2-msmarco --fields text --batch 32 --fp16  # if inference with autocast()


!python -m pyserini.search.faiss \
  --index /content/drive/MyDrive/Run/ \
  --topics /content/drive/MyDrive/queries.jsonl \
  --encoder castorini/tct_colbert-msmarco \
  --output run.msmarco-passage.tct_colbert-v2.bf.tsv \
  --output-format msmarco \
  --batch-size 36 --threads 12
