import secrets
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

tokenForms = secrets.token_hex(16)
app.config['SECRET_KEY'] = tokenForms

if os.getenv('DATABASE_URL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recibos.db'

# ('mysql://root:JCKcEWuUlQXQPHncWAPMBObeEuCTyVna@viaduct.proxy.rlwy.net:34525/railway')

db = SQLAlchemy(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor, faça login para acessar essa página.'
login_manager.login_message_category = 'alert-info'

from PackArquivos import routes
