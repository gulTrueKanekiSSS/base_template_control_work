from flask import Flask, request, render_template

from utils import load_data, search_train
import jsonify
import logging



app = Flask(__name__)

@app.route('/')
def load_main():

    datas = load_data()
    return render_template('index.html', datas=datas)

@app.route('/search_train')
def load_train():

    s = request.args.get('s')
    train = search_train(s)
    return render_template('page_train.html', train=train)
# @app.route("/search")
# def search_post_by_word():
#     s = request.args.get('s')
#     post = search_post(s)
#     return render_template('search.html', post=post)


@app.errorhandler(404)
def error_page(e):
    return 'wtf, it is error 404..'

@app.errorhandler(500)
def error_page_f(e):
    return 'wtf, it is error 500..'


# noinspection PyCallingNonCallable
@app.route("/api/datas")
def api_posts():
    posts = load_data()
    return jsonify(posts)


@app.route("/api/train/<train_name>")
def api_inform(train_name):
    train = search_train(train_name)
    return jsonify(train)


app.run()

# @app.route("/search")
# def search_post_by_word():
#     s = request.args.get('s')
#     post = search_post(s)
#     return render_template('search.html', post=post)

# def search_post(word):
#     data = load_data("data/posts.json")
#     posts = []
#     for post in data:
#         if word.lower() in post['content'].lower():
#             posts.append(post)
#     return posts