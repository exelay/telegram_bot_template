from loguru import logger


logger.add("debug.log", format="{time} {level} {message}", level="INFO", rotation="1 week", compression="zip")
