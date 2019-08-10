import os.path

def check_includes(install_dir):
    logger_py = os.path.sep.join([install_dir, 'logger.py'])
    logging_yaml = os.path.sep.join([install_dir, 'logging.yaml'])
    return os.path.exists(logger_py) and os.path.exists(logging_yaml)
    