from abc import ABC, abstractmethod

from bus_ticket_bot.bot.utils.bot_connection import BotConnection


class BaseHandler(ABC):
    _conn = BotConnection.get_bot()

    @abstractmethod
    def register(self):
        pass
