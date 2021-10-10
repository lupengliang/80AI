import os

from flask import Blueprint, jsonify, send_file

from settings import MongoDB, RET, COVER_PATH, MUSIC_PATH, AVATAR_PATH

get_anything = Blueprint("get_anything", __name__)


@get_anything.route("/get_content_list", methods=["POST"])
def get_content_list():
    content_list = list(MongoDB.content.find({}))

    # 解决ObjectId无法被JSON序列化的问题
    for index, item in enumerate(content_list):
        content_list[index]["_id"] = str(item.get("_id"))

    RET["code"] = 0
    RET["msg"] = "获取内容列表"
    RET["data"] = content_list

    return jsonify(RET)

@get_anything.route("/get_cover/<filename>")
def get_cover(filename):
    file_path = os.path.join(COVER_PATH, filename)
    return send_file(file_path)

@get_anything.route("/get_music/<filename>")
def get_music(filename):
    file_path = os.path.join(MUSIC_PATH, filename)

    return send_file(file_path)

@get_anything.route("/get_avatar/<filename>")
def get_avatar(filename):
    file_path = os.path.join(AVATAR_PATH, filename)

    return send_file(file_path)