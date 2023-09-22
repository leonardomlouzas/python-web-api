from flask_admin.contrib.pymongo import ModelView
from flask_simplelogin import login_required
from wtforms import form, fields, validators
from flask_admin.base import AdminIndexView
from unicodedata import normalize
from blog.database import mongo
from flask_admin import Admin
from datetime import datetime


# Monkey Patch
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
ModelView._handle_view = login_required(ModelView._handle_view)


class PostsForm(form.Form):
    title = fields.StringField("Title", [validators.data_required()])
    slug = fields.HiddenField("Slug")
    content = fields.TextAreaField("Content")
    published = fields.BooleanField("Published", default=True)


class AdminPosts(ModelView):
    column_list = ("title", "slug", "published", "date")
    form = PostsForm

    def on_model_change(self, form, post, is_created):
        post["slug"] = post["title"].replace(" ", "-").replace("_", "-").lower()

        # Removes accents from letters. ç = c
        post["slug"] = normalize("NFKD", post["slug"]).encode('ASCII', 'ignore').decode('ASCII')

        if is_created:
            post["date"] = datetime.now()


def configure(app):
    admin = Admin(
        app,
        name=app.config.get("TITLE"),
        template_mode="bootstrap4"
    )
    admin.add_view(AdminPosts(mongo.db.posts, "Posts"))
