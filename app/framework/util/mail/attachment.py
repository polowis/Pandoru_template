from os.path import basename
class Attachment:
    def __init__(self, path, content_type=None, data=None, disposition=None, headers=None):
        self.content_type = content_type
        self.type = None
        self.data = data or {}
        self.path = path
        self.name = name
        self.disposition = disposition or 'attachment'
        self.headers = headers or {}
    
    def _get_file_name_from_path(self, path):
        self.name = basename(path)
    
    def _init_data(self):
        self._init_filename()._init_mimetype()
    
    def _init_filename(self):
        filename_option = self.data.get('as')
        if filename_option != None:
            self.name = filename_option
        return self
    
    def _init_mimetype(self):
        mimetype_option = self.data.get('mime')
        if mimetype_option != None:
            self.type = mimetype_option
        return self
    


   
   