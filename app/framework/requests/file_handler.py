from flask import request as req
import datetime
from werkzeug.utils import secure_filename

class FileHandler:
    def __init__(self, name):
        self.name = name
        self.file = req.files[self.name]
        self.allow_extension = {'png', 'jpg', 'jpeg'}
        self.filename = ''

    def allow_files(files_list: list):
        """add allow file extension"""
        self.allow_extension = files_list
    
    def is_validated(self):
        """return true if file is valid and is in file allow extension"""
        return '.' in self.file.filename and \
            self.file.filename.rsplit('.', 1)[1].lower() in self.allow_extension
    
    def __secure_file(self):
        """remove space or anything similar"""
        self.filename = secure_filename(self.file.filename.rsplit('.', 1)[0].lower() + str(datetime.datetime.now()) + '.' + self.file.filename.rsplit('.', 1)[1].lower())

    def save(self, src_path):
        """save file to folder"""
        self.__secure_file()
        self.file.save(src_path + self.filename)