from app import app, db
from app.config import Config
from app.framework.util.color import *
import os

@app.cli.command('db:fresh')
def drop_database():
    """Destroys the database and tables."""
    database_url = app.config.get('SQLALCHEMY_DATABASE_URI')
    from sqlalchemy_utils import database_exists, create_database, drop_database
    if database_exists(database_url):
        warn('Dropping database')
        drop_database(database_url)

    if not database_exists(database_url):
        info('Creating database')
        create_database(database_url)

    info('Creating tables.')
    db.create_all()
    info('Refreshed successfully')

