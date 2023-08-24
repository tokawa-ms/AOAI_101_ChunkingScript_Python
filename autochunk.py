import warnings
import tiktoken
import pandas as pd
import glob
import os
import base64
import re
import pyarrow.parquet as pq

from langchain.text_splitter import RecursiveCharacterTextSplitter

enc = tiktoken.get_encoding("cl100k_base")
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base", chunk_size=1000, chunk_overlap=50
)


# テキストファイルを読み込んで、指定のトークン数のチャンクファイルに分割します。
def splitChunkFile(filepath):
    f = open(filepath, "r", encoding="UTF-8")
    data = f.read()
    chunk = text_splitter.split_text(data)

    # chunk単位でループ
    for i, chunkedtext in enumerate(chunk):
        dirname = os.path.dirname(filepath)
        basename = os.path.splitext(os.path.basename(filepath))[0]
        outputfilepath = dirname + "/output/" + basename + "-" + str(i) + ".txt"

        print(i, len(enc.encode(chunkedtext)), outputfilepath)
        with open(outputfilepath, "w", encoding="UTF-8") as fo:
            fo.write(chunkedtext)

        fo.close()
    f.close()

    return


for p in glob.glob("./data/*.txt"):
    splitChunkFile(p)
