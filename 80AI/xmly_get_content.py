import datetime
import logging
import os
import time

import requests

from uuid import uuid4
from settings import HEADERS, CONTENT_LIST_URL, IMAGE_HOST, MUSIC_PATH, COVER_PATH, MongoDB

content_dict = {
    "儿歌": ["424529", "245037"],  # id
    "故事": ["12891461", "260744"],
    "古诗": ["15161417", "12914364"]
}

def get_content_xmly(content_dict: dict):
    # 专辑ID?
    for tag, a_list in content_dict.items():
        for aid in a_list:
            page = 1
            while True:
                content_list = requests.get(CONTENT_LIST_URL % (aid, page), headers=HEADERS).json()
                if not content_list.get("data").get("trackDetailInfos"):
                    break
                page += 1
                content_mongo_list = []
                for content in content_list.get("data").get("trackDetailInfos"):
                    music_name = content.get("trackInfo").get("title")
                    music_file_name = uuid4()
                    music_path = os.path.join(MUSIC_PATH, f"{music_file_name}.mp3")
                    image_path = os.path.join(COVER_PATH, f"{music_file_name}.jpg")
                    music_url = content.get("trackInfo").get("playPath")
                    music_image = IMAGE_HOST + content.get("trackInfo").get("cover")
                    music = requests.get(music_url).content

                    with open(music_path, 'wb') as f:
                        f.write(music)

                    music_image = requests.get(music_image).content

                    with open(image_path, "wb") as f:
                        f.write(music_image)

                    content_info = {
                        "title": music_name,
                        "music": f"{music_file_name}.mp3",
                        "cover": f"{music_file_name}.jpg",
                        "tag": tag,
                        "creatTime": datetime.datetime.now()
                    }
                    content_mongo_list.append(content_info)
                    time.sleep(1.5)
                    logging.warning(f"write end -- {content_info}")
                MongoDB.content.insert_many(content_mongo_list)
get_content_xmly(content_dict)