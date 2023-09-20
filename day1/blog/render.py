from database import conn
from pathlib import Path

# obter os dados
cursor = conn.cursor()
fields = ("id", "title", "content", "author")
results = cursor.execute("SELECT * FROM post;")
posts = [dict(zip(fields, post)) for post in results]

# Criar a pasta de destino do site
site_dir = Path("day1", "blog", "site")
site_dir.mkdir(exist_ok=True)


# Criar função para gerar a url com slug
def get_post_url(post):
    slug = post["title"].lower().replace(" ", "-")
    return f"{slug}.html"


# Renderizar a página index.html
index_template = Path("day1", "blog", "list.template.html").read_text()
index_page = site_dir / Path("index.html")
post_list = [
    f"<li> <a href='{get_post_url(post)}'> {post['title']} </a> </li>"
    for post in posts
]
index_page.write_text(
    index_template.format(post_list="\n".join(post_list))
)

# Renderizar as págindas do blog
for post in posts:
    post_template = Path("day1", "blog", "post.template.html").read_text()
    post_page = site_dir / Path(get_post_url(post))
    post_page.write_text(post_template.format(post=post))

conn.close()
print("Site generated!")
