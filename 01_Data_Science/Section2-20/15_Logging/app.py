import logging

# logging configure

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True,
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('Arithmetic logger')

def add(a, b):
    result = a + b
    logger.debug(f'Addition operation: {a} + {b} = {result}')
    return result

def subtract(a, b):
    result = a - b
    logger.debug(f'Subtraction operation: {a} - {b} = {result}')
    return result

def multiply(a, b):
    result = a * b
    logger.debug(f'Multiplication operation: {a} * {b} = {result}')
    return result

def divide(a, b):
    try:
        result = a / b
        logger.debug(f'Division operation: {a} / {b} = {result}')
        return result
    except ZeroDivisionError:
        logger.error('Cannot divide by zero')
        return None

add(20, 10)
subtract(20, 10)
multiply(20, 10)
divide(20, 10)


