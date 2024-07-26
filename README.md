# Flask-REST
Learning Flask by creating a REST API

`export FLASK_APP=flaskBlog.py`
or for Windows
`set FLASK_APP=flaskBlog.py`

`flask run`


## SQLAlchemy
- from flaskBlog import app, db
- app.app_context().push()
- db.create_all()

### query
- db.session.get(User, 1)