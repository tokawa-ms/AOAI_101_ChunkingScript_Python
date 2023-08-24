import warnings
import tiktoken
import pandas as pd
import glob
import os
import base64
import re
import pyarrow.parquet as pq

from langchain.text_splitter import RecursiveCharacterTextSplitter


def makeDataFrame(filepath):
    f = open(filepath, "r", encoding="UTF-8")
    data = f.read()
    content = " ".join(data.splitlines())

    filename = os.path.basename(filepath)
    enc_id = base64.urlsafe_b64encode(filename.encode())

    return {"id": enc_id.decode(), "content": content, "sourcepage": filename}


df = pd.DataFrame([], columns=["id", "content", "sourcepage"])
data = []

for p in glob.glob("./data/output/*.txt"):
    result = makeDataFrame(p)
    data.append(result)

df = pd.DataFrame(data)
df.to_json(f"chunked_dataset.json", orient="records", force_ascii=False)
