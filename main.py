import os
from os.path import join, dirname
from googlemaps import Client
from dotenv import load_dotenv

load_dotenv(verbose=True)

env_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path=env_path)


GCP_API_KEY = os.environ.get("GCP_API_KEY")
gmaps = Client(key=GCP_API_KEY, requests_kwargs={
                          "headers": {"Accept-Language": "ja-JP"}}) 

# 35.6811673, 139.7670516は東京駅の緯度経度
# Locationは検索の中心点
# Radiusは検索の半径（メートル）
result = gmaps.places(query="駐車場", location=(35.6811673, 139.7670516), radius=1000, language="ja")
items = result["results"]
nextPageToken = result["next_page_token"]

print(items)

"""
# nextPageTokenがある場合は、繰り返し検索する
while "next_page_token" in result:
    result = gmaps.places(query="駐車場", location=(35.6811673, 139.7670516), radius=1000, language="ja", page_token=result["next_page_token"])
    items += result["results"]

# 検索結果の数を取得する
print(len(items))
"""