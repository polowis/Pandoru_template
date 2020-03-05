
"""
Reposible for handling controller files. DO NOT MODIFY!
"""

import os
controller_files = os.listdir('./app/http/controllers')
controllers = {}
files = []

def file_endswith(filename, suffix):
    """Check if file correctly ends"""
    return filename.endswith(suffix) or filename.endswith(suffix.lower())

for controller_file in controller_files:
    filename, file_extension = os.path.splitext(controller_file)
    if file_extension == '.py':
        controllers.update({filename: file_extension})

for controller_name in controllers.keys():
    if file_endswith(controller_name, 'Controller'):
        files.append(controller_name)


__all__ = files



        
