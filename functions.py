import json

POST_PATH = "posts.json"

with open(POST_PATH, "r", encoding="utf8") as files:
    post_json = json.load(files)


def search_post(word):
    post = []
    for posts in post_json:
        if word.lower() in posts.get("content").lower():
            post.append(posts)
    return post



def add_word(words, picture):
    new_post = {"pic": picture, "content": words}
    post_json.append(new_post)
    with open(POST_PATH, mode='w', encoding='utf-8') as file:
        return json.dump(post_json, file, ensure_ascii=False)

