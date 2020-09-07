from app import app
import os

@app.cli.command('config:localization')
def localization():
    os.system("sh app/framework/bin/copy_localization.sh")

@app.cli.command('config:mail')
def mail():
    os.system("sh app/framework/bin/copy_mail.sh")