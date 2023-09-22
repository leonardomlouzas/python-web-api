import click
from blog.posts import (
    get_all_posts,
    get_post_by_slug,
    create_post,
    update_post_by_slug,
    remove_post,
    )


@click.group()
def post():
    """Manage blog posts."""


@post.command()
@click.option("--title")
@click.option("--content")
def new(title, content):
    """Creates a new blog post."""
    new = create_post(title, content)
    click.echo(f"New post created: {new}")


@post.command("list")
def _list():
    """Lists all posts in the blog."""
    for post in get_all_posts():
        click.echo(post)


@post.command()
@click.argument("slug")
def retrieve(slug):
    """List a post by slug."""
    post = get_post_by_slug(slug)
    click.echo(post or "Post not found!")


@post.command()
@click.argument("slug")
@click.option("--content", default=None, type=str)
@click.option("--published", default=None, type=str)
def update(slug, content, published):
    """Updates a post by slug."""
    data = {}
    if content is not None:
        data["content"] = content
    if published is not None:
        data["published"] = published.lower() == "true"
    update_post_by_slug(slug, data)
    click.echo("Post updated")


@post.command()
@click.argument("slug")
def remove(slug):
    """Remove a post from the published list"""
    click.echo(remove_post(slug))


def configure(app):
    app.cli.add_command(post)
