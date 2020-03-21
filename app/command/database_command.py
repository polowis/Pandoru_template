from app import app, db
from app.config import Config
from app.framework.util.color import *
import os
from app.framework.util.faker.fake_generator import FakerGenerator

@app.cli.command('db:fresh')
def reset_database():
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


@app.cli.command('db:migrate')
def migrate_database():
    """Generate migration"""
    os.system('flask db migrate')
    os.system('flask db upgrade')

@app.cli.command('db:fill')
def fill():
    FakerGenerator().generate_fake_users()

@app.cli.command('test')
def test():
    """Run unittest"""
    try:
        import nose2
        os.system('nose2')
    except ImportError:
        error('Nose2 is not installed. Try to run pip install nose2')