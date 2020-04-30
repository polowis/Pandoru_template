from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
import os
csrf = CSRFProtect()

class Configurate:
    
    def __init__(self, app, config, option="config"):
        self.app = app
        self.config = config
        self.SQLALCHEMY_DATABASE_URI = 'SQLALCHEMY_DATABASE_URI'
        if option == "config":
            self.register_config()
        elif option.lower() == "env":
            self.register_env()
        

    def register_env(self):
        """Register environment variable"""   
        if self.__env_file_exists():
            SECRET_KEY = os.getenv('SECRET_KEY')


    def register_app_url(self):
        """Register app url"""
        self.app.config['APP_URL'] = self.config.APP_URL
        self.app.config['APP_PORT'] = self.config.APP_PORT


    def __env_file_exists(self):
        """Return true if .env file exists"""
        dotenv_path = join(dirname(__file__), '.env')
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
            return True
        else:
            raise EnvironmentError('Cannot find .env file')

    def register_config(self):
        """Register config file"""
        self.register_debug()
        self.register_crsf()
        self.register_secret_key()
        self.register_database()
        self.register_sqlalchemy_track_modifications()
        self.register_app_url()
    

    def register_debug(self):
        """Check for debug properties"""
        if self.config.DEBUG_ENABLED:
            self.app.debug = True
    

    def register_crsf(self):
        """Check for csrf properties"""
        if self.config.CSRF_ENABLED:
            csrf.init_app(self.app)


    def register_secret_key(self):
        """Check for secret key"""
        if self.has_existing_key('SECRET_KEY'):
            self.app.secret_key = self.config.SECRET_KEY
    

    def register_database(self):
        """Register database"""
        if self.config.TESTING == True:
            self.app.config[self.SQLALCHEMY_DATABASE_URI] = self.config.DB_TEST
        else:
            if self.has_database_uri():
                self.app.config[self.SQLALCHEMY_DATABASE_URI] = self.config.DB_URI
            else:
                database_support = ['mysql', 'sqlite', 'postgresql', 'oracle', 'firebird', 'sybase']
                if self.config.DB_CONNECTION.lower() in database_support:
                    self.connect_to_database_engine()


    def register_sqlalchemy_track_modifications(self):
        """Register sqlalchemy track modification"""
        if self.has_existing_key('SQLALCHEMY_TRACK_MODIFICATIONS'):
            self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = self.config.SQLALCHEMY_TRACK_MODIFICATIONS


    def connect_to_database_engine(self):
        """Establish a connection to database"""
        if self.config.DB_CONNECTION == 'mysql':
            self.connect_to_mysql()

        if self.config.DB_CONNECTION == 'postgresql':
            self.connect_to_postgresql()
        
        if self.config.DB_CONNECTION == 'sqlite':
            self.connect_to_sqlite()


    def connect_to_sqlite(self):
        """connect to sqlite database"""
        if self.has_database_uri() == False:
            raise Exception('Please provide sqlite db path in config file')


    def connect_to_mysql(self):
        """connect to mysql engine"""
        if self.has_database_uri() == False:
            database_uri = f'{self.config.DB_CONNECTION}://{self.config.DB_USERNAME}:{self.config.DB_PASSWORD}@{self.config.DB_HOST}:{self.config.DB_PORT}/{self.config.DB_DATABASE}'
            self.app.config[self.SQLALCHEMY_DATABASE_URI] = database_uri
    

    def connect_to_postgresql(self):
        """connect to postgresql engine"""
        if self.has_database_uri() == False:
            database_uri = f'postgresql+psycopg2://{self.config.DB_USERNAME}:{self.config.DB_PASSWORD}@{self.config.DB_HOST}:{self.config.DB_PORT}/{self.config.DB_DATABASE}'
            self.app.config[self.SQLALCHEMY_DATABASE_URI] = database_uri
    

    def has_existing_key(self, key: str):
        """Check if environment key exists"""
        members = dir(self.config)
        if key in members:
            if len(key) > 1:
                return True
        return False
        """ error_message = "Expected environment variable '{}' not set in Config file.".format(key)
        raise Exception(error_message)"""
    

    def has_database_uri(self):
        """check if database URI is available in config"""
        if self.has_existing_key('DB_URI'):
            self.app.config[self.SQLALCHEMY_DATABASE_URI] = self.config.DB_URI
            return True
        return False