from app import app
from app.framework.util.color import *
import os
@app.cli.command('serve')
def serve():
    """Serve the application bundled with frontend"""
    os.system('npm run dev')
    os.system('flask run')
