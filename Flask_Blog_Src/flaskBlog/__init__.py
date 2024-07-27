from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__) # name of the module, flask knows where too look for files
CORS(app)

app.config['SECRET_KEY'] = 'dgwrF*5USdWAGr4EqFPqYK'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskBlog import routes