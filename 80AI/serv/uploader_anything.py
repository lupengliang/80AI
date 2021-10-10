import os

from flask import Blueprint, jsonify, send_file, request

from settings import MongoDB, RET, COVER_PATH, MUSIC_PATH, AVATAR_PATH

up_anything = Blueprint("up_anything", __name__)


@up_anything.route("/avatar_uploader", methods=["POST"])
def avatar_uploader():
    avatar = request.files.get("avatar")
    # avatar = request.form.get("avatar")
    # 文件名？
    file_path = os.path.join(AVATAR_PATH, avatar.filename)
    avatar.save(file_path)

    RET["codmsge"] = 0
    RET["msg"] = "头像上传成功"
    RET["data"] = {"filename": avatar.filename}

    return jsonify(RET)