import logging

# Configure logging to both file and console
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    handlers=[
        logging.FileHandler('app1.log'),     # Logs to file
        logging.StreamHandler()             # Logs to console
    ]
)

# Logger for the arithmetic app
logger = logging.getLogger("arithmathicApp")

def add(x, y):
    result = x + y
    logger.debug(f"Adding {x} + {y} = {result}")
    return result

def sub(x, y):
    result = x - y
    logger.debug(f"Subtracting {x} - {y} = {result}")
    return result

def mul(x, y):
    result = x * y
    logger.debug(f"Multiplying {x} * {y} = {result}")
    return result

def div(x, y):
    try:
        result = x / y
        logger.debug(f"Dividing {x} / {y} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Attempted to divide by zero")
        return None

# Test the functions
add(10, 15)
sub(50, 15)
mul(20, 15)
div(30, 15)