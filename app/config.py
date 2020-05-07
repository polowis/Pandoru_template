import os
class Config(object):
    # enable debug
    APP_URL = 'http://localhost'
    APP_PORT = 5000
    DEBUG_ENABLED = False

    #enable testing
    TESTING = False

    #Enable CSRF protection
    CSRF_ENABLED = True

    #App's Key. 
    SECRET_KEY = "50243a674f1d241ee02217580ed14eb524828c95f80e2acc59bd56d6025277ee"

    #Database property
    DB_CONNECTION='mysql'
    DB_HOST='127.0.0.1'
    DB_PORT='3306'
    DB_DATABASE='flask1'
    DB_USERNAME='root'
    DB_PASSWORD=''

    #DB_URI is optional
    # if you use sqlite, you need to specify the path in DB_URI
    DB_URI = f'{DB_CONNECTION}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
    
    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Testing
    DB_TEST=f'{DB_URI}'
    SELENIUM_DRIVER='chrome'

    ## App' locales
    LOCALES = "en"
