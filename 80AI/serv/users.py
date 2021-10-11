import os

from flask import Blueprint, jsonify, send_file, request

from settings import MongoDB, RET, COVER_PATH, MUSIC_PATH

user = Blueprint("user", __name__)


@user.route("/reg", methods=["POST"])
def reg():
    # 接收前端的request数据
    user_info = request.form.to_dict()
    print(user_info)
    user_info["bind_toys"] = []
    user_info["friend_list"] = []

    # 注册接口的逻辑处理
    MongoDB.users.insert_one(user_info)

    # 返回响应客户端
    RET["code"] = 0
    RET["msg"] = "注册成功"
    RET["data"] = {}

    return jsonify(RET)

@user.route('/login', methods=['POST'])
def login():
    user_info = request.form.to_dict()
    # {username:1111,password:2222}
    user = MongoDB.users.find_one(user_info)
    user["_id"] = str(user.get("_id"))

    # 删除password key
    # user = MongoBD.users.find_one(user_info, {"password":0})
    user.pop("password")

    RET["code"] = 0
    RET["msg"] = "登录成功"
    RET["data"] = user

    return jsonify(RET)