"""
DO NOT MODIFY THIS FILE!
"""

from app.framework.controller import Controller
from app.http.exception import view_exception
from app.http.controllers import *

for classes in Controller.__subclasses__():
    classes().construct()
