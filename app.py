from flask import Flask, render_template, request

import functions
from functions import load_data, search_posts, search_name, load_comment, get_post

app = Flask(__name__)


@app.route("/")
def index():
    # загружаем данные
    posts = functions.load_data()
    return render_template("index.html", posts=posts, book_count=5)


@app.route("/search/")
def search_post():
    text = request.args.get('s')
    posts = search_posts(text=text)
    return render_template("index.html", posts=posts)


@app.route("/search/")
def search_name():
    text = request.args.get('s')
    posts = search_name(text=text)
    return render_template("index.html", posts=posts)


@app.route("/post/<int:uid>")
def post(uid):
    # загружаем данные
    post = get_post(uid)
    # загрузка комментариев для поста
    comments = load_comment(post['pk'])

    return render_template("post.html", post=post, comments=comments)


app.run()
