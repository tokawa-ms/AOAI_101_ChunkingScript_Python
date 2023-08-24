import requests
import json as JSON
import os
import glob

# Azure Cognitive Search のインデックス名と API キー
search_service_name = os.environ["SEARCH_SERVICE_NAME"]
index_name = os.environ["SEARCH_INDEX_NAME"]
api_version = "2023-07-01-Preview"
api_key = os.environ["SEARCH_API_KEY"]

# インデックス作成の REST API の URL
createindex_url = "https://{0}.search.windows.net/indexes/{1}?api-version={2}".format(
    search_service_name, index_name, api_version
)

# データをアップロードするための REST API の URL
base_url = (
    "https://{0}.search.windows.net/indexes/{1}/docs/index?api-version={2}".format(
        search_service_name, index_name, api_version
    )
)

url = createindex_url

with open("./create_index.json", "r", encoding="utf-8") as f:
    jsondata = JSON.load(f)
    response = requests.put(
        url,
        headers={"Content-Type": "application/json", "api-key": api_key},
        json=jsondata,
    )
    print(response.status_code, response.text)

files = glob.glob("./chunked_dataset.json")

for file in files:
    print(file)
    with open(file, "r", encoding="utf-8") as f:
        data = JSON.load(f)

        url = base_url
        jsondata = {"value": data}
        response = requests.post(
            url,
            headers={"Content-Type": "application/json", "api-key": api_key},
            json=jsondata,
        )
        print(response.status_code)
        print(response.text)
