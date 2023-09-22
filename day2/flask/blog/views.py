from flask import (
    Blueprint,
    render_template,
    abort,
    request,
    url_for,
    redirect,
    session
)
from blog.posts import (
    get_all_posts,
    get_post_by_slug,
    create_post,
    update_post_by_slug,
    remove_post,
)
from flask_simplelogin import login_required


bp = Blueprint("post", __name__, template_folder="templates")


@bp.route("/")
def index():
    posts = get_all_posts()
    session['teste'] = "ValorQualquer"
    return render_template("index.html.j2", posts=posts)


@bp.route("/<slug>")
def detail(slug):
    post = get_post_by_slug(slug)
    if not post:
        return abort(404, "Post not found")
    return render_template("post.html.j2", post=post)


@bp.route("/new", methods=["GET", "POST"])
@login_required
def new():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        slug = create_post(title, content)
        return redirect(url_for("post.detail", slug=slug))
    return render_template("form.html.j2")


@bp.route("/remove/<slug>", methods=["POST"])
@login_required
def remove(slug):
    deleted_post = remove_post(slug)
    if not deleted_post:
        return abort(404, "Post not found")
    return render_template("post.html.j2", post=deleted_post)


@bp.route("/update/<slug>", methods=["GET", "POST"])
@login_required
def update(slug):
    post = get_post_by_slug(slug)
    if not post:
        return abort(404, "Post not found")

    if request.method == "POST":
        data = {}
        content = request.form.get("content")
        published = request.form.get("published")

        if content:
            data["content"] = content
        if published:
            data["published"] = published

        update_post_by_slug(slug, data)
        return redirect(url_for("post.detail", slug=slug))
    return render_template("update.html.j2", post=post)


def configure(app):
    app.register_blueprint(bp)
