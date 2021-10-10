# 喜马拉雅数据采集工具参数
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}

CONTENT_LIST_URL = 'https://m.ximalaya.com/m-revision/common/album/queryAlbumTrackRecordsByPage?albumId=%s&page=%s&pageSize=20'
IMAGE_HOST = "http://imagev2.xmcdn.com/"


# 目录配置
import os
COVER_PATH = os.path.join("data", "cover")
MUSIC_PATH = os.path.join("data", "music")
AVATAR_PATH = os.path.join("data", "avatar")

# 数据库配置
from pymongo import MongoClient
MC = MongoClient()
MongoDB = MC["80AI"]

# Return 配置
RET = {"code": 0, "msg": "", "data": {}}