try:
    from app.configuration.localization import *
except ImportError:
    print("The localization file could not be found")

from flask import request as req
from app.config import Config
from ...util import *
import json
import os


DEFAULT_LOCALES = [Config.LOCALES]

class Localization:
    def __init__(self):
        self.supported_locales = locales_support.keys()
        self.supported_locales_names = locales_support.values()
        
    def get_supported_locales(self) -> dict:
        """return dictionary of supported locales"""
        locales = locales_support
        if isinstance(locales, dict):
            return locales
        raise TypeError("Supported locales is not defined")
    
    def get_current_locales(self) -> str:
        """Return supported accept_language
        Note: this only check for supported language in config file.
        """
        locales = self.get_supported_locales().keys()
        if(len(locales) < 1):
            return req.accept_languages.best_match(DEFAULT_LOCALES)
        else:
            return req.accept_languages.best_match(locales)

    def get_current_locales_name(self) -> str:
        """Return the current locales name as a string"""
        locales = self.get_supported_locales()
        return locales[self.get_current_locales()]
    
    def get_supported_locales_key(self) -> list:
        """Return an array with all the keys for the supported locales."""
        return locales_support.keys()

    def lang(self, key: str, **kwargs):
        """get translation for given key"""
        locales = DEFAULT_LOCALES 
        log(kwargs)
        if locales is None:
            locales = self.get_current_locales()

        fileName = self.get_file_name(key)[0]
        try:
            response = self.read_file(locales, fileName, key)
            return self.handle_placeholder(response, **kwargs)
        except IOError:
            pass
        try:
            response = self.read_file('en', fileName, key)
            return self.handle_placeholder(response, **kwargs)
        except IOError:
            raise Exception("Unable to read file, if you don't use localization, you can disable it")


    def get_file_name(self, fileName: str) -> list:
        """get file name, likely will be deprecated"""
        return fileName.split(".")

    def get_property(self, path):
        """get all properties, exclude fileName"""
        properties = self.get_file_name(path)
        properties.remove(properties[0])
        return properties
    
    def read_file(self, locales: str, fileName: str, pathFile):
        """Read translated file, must be in JSON format"""
        path = f"app/resources/lang/{locales}/{fileName}.json"
        with open(path) as file:
            data = json.load(file)
    
        return self.find(self.get_property(pathFile), data)

    def find(self, element, json):
        """Find by dot notation"""
        keys = element
        rv = json
        for key in keys:
            rv = rv[key]
        return rv
    
    def handle_placeholder(self, string: str, **kwargs):
        """Replace placeholder
        for eg: Hello :name, name="John" => Hello John
        """
        element = string.split()
        for index in range(len(element)):
            if element[index].startswith(":"):
                var = element[index][1:]
                if kwargs.get(var) is not None:
                    element[index] = kwargs.get(var)

        return ' '.join(element)