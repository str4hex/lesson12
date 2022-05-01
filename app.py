from flask import Flask, request, render_template, send_from_directory
from functions import search_post
from main.main import main
from loader.loader import loader
import logging


app = Flask(__name__)

app.register_blueprint(loader)
app.register_blueprint(main)


@app.route("/search")
def search():
    search = request.values['s']
    post = search_post(search)
    logging.info(search)
    return render_template("post_list.html", post=post, search=search)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
