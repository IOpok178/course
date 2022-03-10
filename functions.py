import json
import pprint


def load_data():
    # загрузка данных
    with open("data/data.json", encoding='utf8') as f:
        data = json.load(f)
    return data


def search_posts(text):
    # поиск поста
    data = load_data()
    posts = []

    for post in data:
        if post["content"].find(text) != -1:
            posts.append(post)

    return posts


def search_name(user_name):
    # поиск поста пользователя
    data = load_data()
    name = []

    for post in data:
        if post["poster_name"] == user_name:
            name.append(post)

    return name


def load_comment(post_id):
    # загрузка комментариев
    with open("data/comments.json", encoding='utf8') as f:
        data = json.load(f)
        comments = []

    for comment in data:
        if comment['post_id'] == post_id:
            comments.append(comment)

    return comments


def get_post(uid):
    # найти пост по идентификатору
    posts = load_data()

    for post in posts:
        if post['pk'] == uid:
            return post
    return None
