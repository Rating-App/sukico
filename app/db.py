import os

#from app import app
from flask_sqlalchemy import SQLAlchemy
from . import app

def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

# the values of those depend on your setup
POSTGRES_URL = get_env_variable("POSTGRES_URL")
POSTGRES_USER = get_env_variable("POSTGRES_USER")
POSTGRES_PW = get_env_variable("POSTGRES_PW")
POSTGRES_DB = get_env_variable("POSTGRES_DB")

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,
                                                                 pw=POSTGRES_PW,
                                                                url=POSTGRES_URL,
                                                                 db=POSTGRES_DB)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Silence the warning
db = SQLAlchemy(app)

@app.cli.command('resetdb')
def resetdb_command():
    """Destroys and creates the database + tables."""

    # TODO: insufficient privilidges???
    #from sqlalchemy_utils import database_exists, create_database, drop_database
    #if database_exists(DB_URL):
    #    print('Deleting database.')
    #    drop_database(DB_URL)
    #if not database_exists(DB_URL):
    #    print('Creating database.')
    #    create_database(DB_URL)

    print('Creating tables.')
    db.create_all()
    print('Shiny!')

