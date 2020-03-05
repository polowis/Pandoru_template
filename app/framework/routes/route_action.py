

def getModule(string):
    module_name = string.rsplit('.', 1)[0]
    return module_name

def getFunction(string):
    function_name = string.rsplit('.', 1)[1]
    return function_name


