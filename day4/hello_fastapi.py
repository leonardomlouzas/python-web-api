from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class ListOption(str, Enum):
    user = "user"
    department = "department"
    account = "account"


@app.get("/{list_option}/list")
async def generic_list(list_option: ListOption):
    print(list_option)
    if list_option == ListOption.user:
        data = ["Jim", "Pam", "Dwight"]
    elif list_option == ListOption.department:
        data = ["Sales", "Management", "IT"]
    elif list_option == ListOption.account:
        data = [124, 123, 12]

    return {list_option: data}


@app.get("/user/{username}")
async def user_profile(username: str):
    return {"data": username}


@app.get("/account/{number}")
async def account_detail(number: int):
    return {"account": number}


@app.get("/import/{file_path:path}")
def import_file(file_path: str):
    return {"importing": file_path}
