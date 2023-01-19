import json

def load_data():
    with open('data1.json') as file:
        data = json.load(file)
    return data

def data_by_day(day):
    data = load_data()
    sorted_data_day = []
    for dat in data:
        if dat['days'] == day:
            sorted_data_day.append(dat)
    return  sorted_data_day

def search_train(train_name):
        data = load_data()
        trains = []
        for train in data:
            if train_name.lower() in train['train'].lower():
                trains.append(train)
        return trains



# def search_post(word):
#     data = load_data("data/posts.json")
#     posts = []
#     for post in data:
#         if word.lower() in post['content'].lower():
#             posts.append(post)
#     return posts

# def load_comments(post_id):
#     data = load_data("data/comments.json")
#     comments = []
#     for comment in data:
#         if comment["post_id"] == post_id:
#             comments.append(comment)
#     return comments
#
# def get_post_by_pk(pk):
#     data = load_data("data/posts.json")
#     posts = []
#     for post in data:
#         if post['pk'] == pk:
#             posts.append(post)
#     return posts
#
# def search_post(word):
#     data = load_data("data/posts.json")
#     posts = []
#     for post in data:
#         if word.lower() in post['content'].lower():
#             posts.append(post)
#     return posts
#
# def get_profile_by_name(name):
#     data = load_data("./data/posts.json")
#     posts = []
#     for post in data:
#         if name in post['poster_name']:
#             posts.append(post)
#     return posts