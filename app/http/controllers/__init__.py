

import os
controller_files = os.listdir('./app/http/controllers')
controllers = {}
files = []

for controller_file in controller_files:
    filename, file_extension = os.path.splitext(controller_file)
    if file_extension == '.py':
        controllers.update({filename: file_extension})

for controller_name in controllers.keys():
    if controller_name.endswith('Controller') or controller_name.endswith('controller'):
        files.append(controller_name)


__all__ = files



        
