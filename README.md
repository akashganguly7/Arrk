# Arrk

Run the following commands to setup db:

===========================================================
===========================================================

cd to project folder
python run.py

===========================================================
===========================================================
to setup venv
python3 -m venv venv
pipenv3 install flask
pip3 install flask_sqlalchemy

===========================================================
===========================================================

if DB setup is required
cd to project folder
python
>>> from run import db, create_app
>>> db.create_all(app = create_app())

Check DB tables
sqlite3 data.sqlite3
sqlite> .tables

(user table should be visible)

===========================================================
===========================================================
