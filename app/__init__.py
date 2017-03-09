from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_login import LoginManager
# from flask_openid import OpenID
# from config import basedir
# import os

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


lm = LoginManager()
lm.init_app(app)
lm.session_protection = 'strong'
lm.login_view = 'login'
# oid = OpenID(app, os.path.join(basedir, 'tmp'))

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()

bootstrap.init_app(app)
mail.init_app(app)
moment.init_app(app)
# db.init_app(app)


from app import views, models