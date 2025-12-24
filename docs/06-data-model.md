# 06 - Data Model

## Overview
This document describes the database schema for the Bus Ticket Telegram Bot.  
The data model is designed to support the complete flow of ticket sales, purchases, refunds, and admin operations.  
All entities are related to tickets as the central concept, and relationships ensure data integrity while supporting business logic.

The main entities are:
- `Tickets`: All available tickets for sale.
- `Users`: Buyers using the Telegram bot.
- `Purchased_Tickets`: Records of ticket purchases.
- `Refund_Requests`: Refund request records.
- `Admins`: Operators managing tickets and transactions.
- `Bot_Instance`: Bot configuration and message templates.

---

## Tables / Entities

### Tickets
| Column             | Type     | Description / Constraints                 |
|-------------------|----------|-------------------------------------------|
| id                | integer  | Primary Key                               |
| name              | string   | Ticket name                               |
| ticket_type       | string   | One of [VIP, NORMAL, CAR]                 |
| origin_city       | string   | Foreign Key → Bot_Instance(city_name)     |
| origin_terminal   | string   | Foreign Key → Bot_Instance(terminal_name) |
| city              | string   | Destination city                          |
| destination_terminal | string   | Optional                                  |
| date              | datetime | Format: YYYY-MM-DD HH:MM:SS        |
| price             | integer  | Must be greater than 0                    |
| created_at        | datetime | Default = CURRENT_DATE                    |

---

### Users
| Column      | Type     | Description / Constraints                  |
|-------------|----------|--------------------------------------------|
| id          | integer  | Primary Key, Auto Increment                |
| full_name   | string   | Optional                                   |
| telegram_id | integer  | Unique                                     |
| state       | string   | Default = "Inactive"                        |
| warnings    | integer  | Default = 0 (user banned after 3 warnings) |
| created_at  | datetime | Default = CURRENT_DATE                     |

---

### Purchased_Tickets
| Column         | Type    | Description / Constraints                                    |
|----------------|---------|--------------------------------------------------------------|
| id             | integer | Primary Key, Auto Increment                                  |
| telegram_id    | integer | Foreign Key → Users(telegram_id)                             |
| ticket_id      | integer | Foreign Key → Tickets(id)                                    |
| user_id        | integer | Foreign Key → Users(id)                                      |
| transaction_id | integer | Generated unique key                                         |
| active         | boolean | Default = False                                              |
| receipt        | string  | Telegram message ID linking to receipt in Transactions Group |
| created_at     | datetime| Default = CURRENT_DATE                                       |

---

### Refund_Requests
| Column            | Type    | Description / Constraints                      |
|-------------------|---------|------------------------------------------------|
| id                | integer | Primary Key                                    |
| transaction_id    | integer | Foreign Key → PurchasedTickets(transaction_id) |
| telegram_id       | integer | Foreign Key → Users(telegram_id)               |
| receipt_id        | string  | Foreign Key → Purchased_Tickets(receipt)       |
| refund_request_id | string  | Telegram message ID                            |
| reason            | string  | Optional                                       |
| created_at        | datetime| Date of request                                |

---

### Admins
| Column       | Type    | Description / Constraints        |
|-------------|---------|---------------------------------|
| id          | integer | Primary Key                     |
| full_name   | string  | Optional                        |
| telegram_id | integer | Unique                           |
| created_at  | datetime| Default = CURRENT_DATE           |

---

### Bot_Instance
| Column             | Type    | Description                       |
|-------------------|---------|----------------------------------|
| id                | integer | Primary Key                       |
| name              | string  | Company / Transit name            |
| address           | text    | Address of company                |
| call_number       | integer | Contact number                     |
| terminal_name     | string  | Name of terminal                   |
| city_name         | string  | City where bot operates            |
| start_message     | text    | Message shown on /start            |
| contact_us_message| text    | Message shown on Contact Us        |
| help_message      | text    | Message shown on /help             |
| payment_message   | text    | Payment instruction message         |
| refund_message    | text    | Refund instruction message          |

---

## Relationships
- `Tickets (1)` → `Purchased_Tickets (N)`
- `Users (1)` → `Purchased_Tickets (N)`
- `Refound_Requests.telegram_id (1)` → `Users.telegram_id` 
- `Purchase_Tickets.telegram_id (1)` → `Users.telegram_id` 
- `Refound_Requests.transaction_id (1)` → `Purchased_Tickets.transaction_id` 
- `Purchased_Tickets (1)` → `Refund_Requests (0..1)`
- `Tickets.origin_city` → `Bot_Instance.city_name`
- `Tickets.origin_terminal` → `Bot_Instance.terminal_name`
- `Admins` manage `Tickets` and `Purchased_Tickets`
- `Bot_Instance` stores global configuration used by all other entities

---

## ERD (Textual Representation)
