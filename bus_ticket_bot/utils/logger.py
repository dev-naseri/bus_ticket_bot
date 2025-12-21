import logging
from bus_ticket_bot.config.settings import BOT_LOGGER, SERVICES_LOGGER

class Logger:
    _bot_logger = None
    _service_logger = None

    class _LoggerProperty:
        def __init__(self, name, filename):
            self.name = name
            self.filename = filename
            self._logger = None

        def __get__(self, instance, owner):
            if self._logger is None:
                self._logger = logging.getLogger(self.name)
                handler = logging.FileHandler(self.filename)
                formatter = logging.Formatter(
                    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                )
                handler.setFormatter(formatter)
                self._logger.addHandler(handler)
                self._logger.setLevel(logging.DEBUG)
            return self._logger

    bot = _LoggerProperty("bot", BOT_LOGGER)
    service = _LoggerProperty("service", SERVICES_LOGGER)
