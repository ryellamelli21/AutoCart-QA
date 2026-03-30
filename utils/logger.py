import logging


def get_logger():
    logger = logging.getLogger("seleniumforge")

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler("reports/test.log")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger