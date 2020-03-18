from app import app
import bcrypt
from app.framework.util.color import *
import click

@app.cli.command('hash')
@click.argument('password')
def hash(password: str):
    hash_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    info('The encrypted string is:')
    warn(str(hash_password))
