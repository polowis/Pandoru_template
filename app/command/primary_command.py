from app import app
from app.framework.util.color import *
import os
import time

@app.cli.command('serve')
def serve():
    """Serve the application bundled with frontend"""
    os.system('npm run dev')
    os.system('flask run')

@app.cli.command('node')
def node():
    """Start node server """
    warn('Make sure you have node install...')
    time.sleep(2)
    os.system('sh ./bin/redis.sh')
    os.system('npm run serve')