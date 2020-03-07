from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()
class Configurate:
    
    def __init__(self, app, config):
        self.app = app
        self.config = config
        self.register()
    
    def register(self):
        """Register config file"""
        self.register_debug()
        self.register_crsf()
        self.register_secret_key()
    
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
        self.app.secret_key = self.config.SECRET_KEY
        