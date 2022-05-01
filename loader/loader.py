import logging
from flask import Blueprint, render_template, request
from functions import add_word
from error import ImageError
loader = Blueprint("loader", __name__)
UPLOAD_FOLDER = "uploads/images"



@loader.route("/loader")
def loaders():
    return render_template("post_form.html")


@loader.route("/post", methods=["GET", "POST"])
def loader_post():
    picture = request.files["picture"]
    extension = picture.filename.split(".")[-1]
    words = request.values["content"]
    if not picture or not words:
        logging.info("Данные  не загружены, не указана картинка и сообщение")
        return "нет данных"
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    if extension in ALLOWED_EXTENSIONS:
        picture.save(f"./uploads/images/{picture.filename}")
        picture_save = f"./{UPLOAD_FOLDER}/{picture.filename}"
    else:
        return "Загруженный файл - не картинка (расширение не jpeg и не png)"


    add_word(words,picture_save)
    return render_template("post_uploaded.html", picture_save=picture_save, words=words)
