python -m pyserini.eval.trec_eval -c -mrecall.1000 -mmap msmarco-passage-dev-subset \
    runs/run.msmarco-passage.ance.bf.trec
