flask commands:

pip install -e .
flask run --debug
flask shell
docker run -d -p 27017:27017 --name mongo-blog mongo:latest
FLASK_ENV=development FLASK_APP=blog.app:create_app flask routes

-----------------------------------------------------------------------

libraries:
asttokens==2.4.0
backcall==0.2.0
blinker==1.6.2
click==8.1.7
decorator==5.1.1
dnspython==2.4.2
dominate==2.8.0
dynaconf==3.2.3
executing==1.2.0
Flask==2.3.3
Flask-Admin==1.6.1
-e git+ssh://git@github.com/leonardomlouzas/python-web-api.git@9977bdccb29c564eaff288979fd41328613bdcf3#egg=flask_blog&subdirectory=day2/flask
Flask-Bootstrap==3.3.7.1
Flask-PyMongo==2.3.0
flask-shell-ipython==0.5.1
flask-simplelogin==0.1.2
Flask-WTF==1.1.1
ipython==8.15.0
itsdangerous==2.1.2
jedi==0.19.0
Jinja2==3.1.2
MarkupSafe==2.1.3
matplotlib-inline==0.1.6
mistune==3.0.1
parso==0.8.3
pexpect==4.8.0
pickleshare==0.7.5
prompt-toolkit==3.0.39
ptyprocess==0.7.0
pure-eval==0.2.2
Pygments==2.16.1
pymongo==4.5.0
six==1.16.0
stack-data==0.6.2
traitlets==5.10.0
visitor==0.1.3
wcwidth==0.2.6
Werkzeug==2.3.7
WTForms==3.0.1
