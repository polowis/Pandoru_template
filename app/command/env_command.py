from app import app
from app.framework.util.color import *
import os

@app.cli.command('key:generate')
def generate_key():
    """Generate a new app key"""
    info('Here is the new key, you may copy and paste it in your config environment: \n')
    warn(os.urandom(32).hex())