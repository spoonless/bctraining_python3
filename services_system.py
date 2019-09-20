import hug
import system_info
import logging
import logging.config

logging.config.fileConfig("log.ini")
logger = logging.getLogger(__name__)

def log_exception(f):
    def decorateur(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            logger.exception(e)
            raise

    return decorateur

@hug.get("/system/info")
@log_exception
def get_system_info():
    logger.info("start - info système pour la machine")
    sys_info = system_info.get_info()
    logger.info("start - info système pour la machine")
    return sys_info

