from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify
from blog.models import Post


class Command(BaseCommand):
    """Adds new post into the Database"""

    help = "Creates a new post into the Database"

    def add_arguments(self, parser):
        parser.add_argument("--title", type=str, required=True)
        parser.add_argument("--content", type=str, required=True)

    def handle(self, *args, **options):
        try:
            post = Post.objects.create(
                title=options["title"],
                content=options["content"],
                slug=slugify(options["title"]),
            )
        except Exception as e:
            raise CommandError(e)
        else:
            self.stdout.write(self.style.SUCCESS(f"Created post: {post.title}"))
