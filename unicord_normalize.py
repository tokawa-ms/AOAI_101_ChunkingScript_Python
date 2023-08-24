import unicodedata
import glob


# テキストファイルを読み込んで、指定のトークン数のチャンクファイルに分割します。
def splitChunkFile(filepath):
    print(filepath)
    f = open(filepath, "r", encoding="UTF-8")
    data = f.read()
    f.close()

    # filepath からファイル名だけ抽出
    filename = filepath.split("\\")[-1]
    # ファイル名から拡張子を除去
    filename = filename.split(".")[0]
    # ファイルのパスだけを変数に抽出
    dirname = "\\".join(filepath.split("\\")[:-1])

    filepath2 = dirname + "\\normalized\\" + filename + ".txt"
    print(filepath2)

    f2 = open(filepath2, "w", encoding="UTF-8")

    # data を正規化
    data = unicodedata.normalize("NFKC", data)
    f2.write(data)
    f2.close()
    return


for p in glob.glob(".\\data\\*.txt"):
    splitChunkFile(p)
