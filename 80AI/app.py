from flask import Flask

from serv.get_anythings import get_anything
from serv.uploader_anything import up_anything
from serv.user import user

app = Flask(__name__)

app.config["DEBUG"] = True

app.register_blueprint(get_anything)
app.register_blueprint(user)
app.register_blueprint(up_anything)


if __name__ == '__main__':
    app.run("0.0.0.0", 9527)