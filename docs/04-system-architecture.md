# System Architecture

## Architectural Overview

This project follows a **bot-centric** and **state-driven** architecture.  
Given the intended scope, business requirements, and expected usage scale, the system is designed as a **single-instance, non-distributed application**.

The primary architectural goal is **clarity, simplicity, and reliability**, rather than high scalability or distributed processing.  
All user interactions are mediated through a Telegram bot, which acts as the central coordination point for both passengers and administrators.

---

## Core Components

- **Python 3.12**
- **pyTelegramBotAPI 4.29.1**
- **Peewee 3.18.3 (ORM)**

---

### Telegram Bot Interface

The Telegram bot serves as the **entry point** of the system and the primary communication channel between passengers and administrators.

From the passenger perspective, the bot enables users to:
- Select a destination and travel time
- Submit required personal information
- Complete payment via card-to-card transfer
- Receive ticket activation and a unique reservation code after admin approval

Once a transaction is verified and approved by the admin, the ticket is activated and associated with a unique identifier that the passenger can later use for validation.

The architectural focus of the bot layer is on **responsibility separation and flow control**, rather than low-level implementation details.

---

### Admin Interaction Layer

Administrators interact with the system through the **same Telegram bot** used by passengers.  
Access control and privilege separation are enforced based on the administrator’s **Telegram ID**.

Role-based behavior is predefined and aligned with operational workflows commonly used by small transit companies or local transportation groups.  
This approach avoids the need for a separate admin application while maintaining clear responsibility boundaries.

---

### Data Persistence Layer

SQLite is selected as the primary data storage solution.

The **Peewee ORM** is used to:
- Define and manage data models
- Enforce relationships and constraints
- Provide a clear abstraction layer between business logic and persistent storage

This choice supports simplicity, maintainability, and low operational overhead.

---

### Telegram Transactions Group

All payment receipts—submitted as images or text messages by passengers—are forwarded by the bot to a dedicated **Telegram transactions group**.

This group serves as:
- A centralized audit trail for all financial transactions
- A review interface for administrators

Each transaction message is linked to database records via Telegram `message_id` references.  
After verifying the transaction within the group, the admin approves the payment, which triggers automated handling by the bot (e.g., ticket activation).

---

## High-Level Data Flow

1. User initiates an action via the Telegram bot  
2. Bot validates input and processes the request  
3. Relevant data is stored or updated in the database  
4. Admin reviews and approves transactions  
5. Bot sends confirmation and updates ticket status  

---

## User Interaction Model

The ticket purchase process is fully **state-based and stateful**.

Because Telegram bots operate in a conversational context, each interaction step depends on the successful completion of the previous one.  
This ensures:
- Data consistency
- Validation at each stage
- Reduced user confusion

Overall, the system follows a **dialog-driven interaction model**.

---

## Admin Interaction Model

Administrators operate through a dedicated control flow within the bot, distinct from passenger interactions.

While the admin workflows are also **state-based and stateful**, they focus on:
- Ticket creation and modification
- Payment approval
- Message and ticket management

Payment confirmations are performed directly within the Telegram transactions group.  
Admins also retain full control over user-facing messages and ticket-related communications.

---

## Error Handling and Edge Cases

- **Capacity Management**  
  Ticket capacity may change due to offline (in-person) sales. For this reason, capacity adjustments are handled manually by the admin.  
  When capacity is fully consumed within the bot, the ticket is automatically removed from the available purchase options.

- **Invalid Payments**  
  Payment validation relies on manual admin verification of card-to-card transfers before ticket activation.

- **Cancellation Policy**  
  Ticket cancellation is allowed only up to **two hours before departure**.  
  The bot strictly enforces this policy during cancellation requests.

- **Expired or Invalid Tickets**  
  Tickets that are no longer valid (e.g., after departure) are automatically removed from active user views.

---

## Architectural Constraints and Trade-offs

- **SQLite Usage**  
  SQLite is intentionally chosen to keep the system lightweight and easy to deploy, as the expected scale and deployment environment do not justify more complex database solutions.

- **Manual Payment Process**  
  Card-to-card payment confirmation is implemented based on client requirements and local user trust patterns, particularly in small cities.

- **Limited Scalability**  
  The architecture is deliberately kept non-scalable.  
  The system is not expected to undergo major structural changes or serve high-volume usage, and the current design adequately supports its long-term goals.

---

## Extensibility Considerations

- The system can be migrated to more advanced database solutions if future requirements demand it.
- Online payment gateways can be integrated without major architectural changes.
- Due to its object-oriented and modular design, the system allows for the addition of new business rules and features with minimal refactoring.
