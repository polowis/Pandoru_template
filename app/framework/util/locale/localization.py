try:
    from app.configuration.localization import *
except ImportError:
    print("The localization file could not be found")

from flask import request as req

DEFAULT_LOCALES = ["en-US"]

class Localization:
    def __init__(self):
        self.supported_locales = locales_support.keys()
        self.supported_locales_names = locales_support.values()
        
    def get_supported_locales(self):
        """return dictionary of supported locales"""
        locales = locales_support
        if isinstance(locales, dict):
            return locales
        raise TypeError("Supported locales is not defined")
    
    def get_current_locales(self):
        """Return supported accept_language
        Note: this only check for supported language in config file.
        """
        locales = self.get_supported_locales().keys()
        if(len(locales) < 1):
            return req.accept_languages.best_match(DEFAULT_LOCALES)
        else:
            return req.accept_languages.best_match(locales)

    def get_current_locales_name(self):
        """Return the current locales name as a string"""
        locales = self.get_supported_locales()
        return locales[self.get_current_locales()]
    
    def get_supported_locales_key(self):
        """Return an array with all the keys for the supported locales."""
        return locales_support.keys()
