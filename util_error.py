from util_asciiart import error_handler
import util_constants as constant

def err(er, fi):
    return f"{error_handler}Error from {fi}.py\n{er}"

def throw(error, file):
    full_error = err(error, file)
    raise Exception(full_error)

def passE(error, file):
    if constant.devmode:
        print(err(error, file))