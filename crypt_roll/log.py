import logging


class CryptRollLogger(logging.getLoggerClass()):
    EGG_LEVEL=15
    def egg(self, msg, *args, **kwargs):
        self.log(self.EGG_LEVEL, msg, *args, **kwargs)


def get_logger(name, level=20):
    logger = CryptRollLogger(__name__)
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(level)
    return logger