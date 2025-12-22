from bus_ticket_bot.models.users import Users
from bus_ticket_bot.services.users_service import UsersService

r = UsersService.select(id=1)
t = r.data.created_at
print(t)
