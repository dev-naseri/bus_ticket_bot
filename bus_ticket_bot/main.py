from xml.sax import ContentHandler

from bus_ticket_bot.bot.handlers.contact_us_handler import ContactUsHandler
from bus_ticket_bot.bot.handlers.help_handler import HelpHandler
from bus_ticket_bot.bot.handlers.start_handler import StartHandler
from bus_ticket_bot.bot.utils.bot_connection import BotConnection


StartHandler.register()
HelpHandler.register()
ContactUsHandler.register()


BotConnection.get_bot().infinity_polling()