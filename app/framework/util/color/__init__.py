class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def error(message: str):
    """Display error messsage"""
    print('\033[31m' + message)

def info(message: str):
    """Display info message"""
    print('\033[92m' + message)

def warn(message: str):
    """Display warn message"""
    print('\033[93m' + message)

class Command(object):
    def construct(cls):
        cls.construct()