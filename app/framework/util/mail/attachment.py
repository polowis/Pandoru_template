class Attachment:
     def __init__(self, filename=None, content_type=None, data=None, disposition=None, headers=None):
        self.filename = filename
        self.content_type = content_type
        self.data = data
        self.disposition = disposition or 'attachment'
        self.headers = headers or {}