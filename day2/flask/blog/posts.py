from unicodedata import normalize
from blog.database import mongo
from datetime import datetime
import pymongo


def get_all_posts(published: bool = True):
    posts = mongo.db.posts.find({"published": published})

    return posts.sort("date", pymongo.DESCENDING)


def get_post_by_slug(slug: str) -> dict:
    post = mongo.db.posts.find_one({"slug": slug})
    return post


def update_post_by_slug(slug: str, data: dict) -> dict:
    return mongo.db.posts.find_one_and_update({"slug": slug}, {"$set": data})


def create_post(title: str, content: str, published: bool = True) -> str:
    slug = title.replace(" ", "-").replace("_", "-").lower()

    # Remove accents from letters. ç = c
    slug = normalize("NFKD", slug).encode('ASCII', 'ignore').decode('ASCII')

    found_post = mongo.db.posts.find_one({"title": title.capitalize()})

    if found_post:
        return "Post com mesmo título já existe, operação cancelada."

    mongo.db.posts.insert_one(
        {
            "title": title.capitalize(),
            "content": content,
            "published": published,
            "slug": slug,
            "date": datetime.now(),

        }
    )
    return slug


def remove_post(slug: str) -> str:
    return mongo.db.posts.find_one_and_update({"slug": slug}, {"$set": {"published": "false"}})