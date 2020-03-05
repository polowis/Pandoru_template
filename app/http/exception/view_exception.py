from flask import render_template
from app import app


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html')

@app.errorhandler(500)
def page_not_found(e):
    return render_template('error/500.html')