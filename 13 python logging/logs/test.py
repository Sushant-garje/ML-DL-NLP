from logger import logging

def add(x,y):
    logging.debug('addition operation is performed')
    return x+y

logging.debug("calling the add function")
add(23,43)