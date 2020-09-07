from app import app
import os
from app.framework.util.color import *

@app.cli.command('config:localization')
def localization():
    os.system("sh app/framework/bin/copy_localization.sh")
    info("Successfully generated localization config file")
    

@app.cli.command('config:mail')
def mail():
    os.system("sh app/framework/bin/copy_mail.sh")
    info("Successfully generated mailing config file")