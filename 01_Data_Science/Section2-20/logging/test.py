from logger import logging

def addition(a, b):
    logging.debug('Addition operation is being taking place')
    return a + b

logging.debug('Addition function is being called')
addition(10, 15)
