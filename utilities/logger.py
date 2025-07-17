import inspect, logging
from logging import DEBUG

def custom_logger(log_level= logging.DEBUG):
    # gets the name of the class / method from where the method is called

    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    # By default, log all messages
    logger.setLevel(logging.DEBUG)


    file_handler = logging.FileHandler("automation.log", mode='a')
    file_handler.setLevel(log_level)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s",
                                  datefmt='%d/%m/%Y %H:%M:%S')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger