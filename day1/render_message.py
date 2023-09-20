from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader("."))

template = env.get_template("email.template.txt")


def addhearts(text):
    return f"❤️ {text} ❤️"


env.filters["addhearts"] = addhearts

data = {
    "name": "Bruno",
    "products": [
        {"name": "Iphone", "price": 13000.320},
        {"name": "Ferrari", "price": 9000000.420},
    ],
    "special_customer": True
}

print(template.render(**data))
