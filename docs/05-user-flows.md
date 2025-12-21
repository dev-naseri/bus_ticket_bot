# User Flows

## Overview

This document describes the expected behavior and interaction paths of both **passengers** and **administrators** within the system.

The primary goal of these flows is to:
- Clarify user and admin decision paths
- Anticipate user behavior and system responses
- Minimize user confusion
- Reduce the time required for passengers to successfully purchase tickets
- Simplify ticket and transaction management for transit operators

All user interactions are designed with the assumption that passengers may have **limited technical knowledge**, and therefore require clear, guided, and step-by-step flows.

---

## Passenger (Buyer) Flows

When a passenger starts the bot, they are presented with a clear welcome message explaining the purpose of the system.

Given the assumed low technical familiarity of most users, the system actively guides passengers toward the `/help` section, where the ticket purchase process is explained in a simple and structured manner.

Upon first interaction, a user profile is automatically created in the database.  
The passenger is then granted access to a ticket management panel, where they can:
- Purchase tickets based on available destinations
- View the status of previously purchased tickets
- Request cancellations when permitted

---

### Passenger Entry Flow

The passenger initiates the ticket purchase process by progressing through the following steps:

1. Ticket type selection  
2. Date selection  
3. Time selection  
4. Capacity validation  

Only tickets with available capacity are presented to the user.

---

### Ticket Purchase Flow

During the ticket purchase process, the system performs the following steps:

1. Display ticket details and request purchase confirmation  
2. Collect the number of passengers  
3. Collect passenger full name(s)  
4. Collect a valid mobile phone number  
5. Determine passenger residency status (local or non-local)  
6. Collect national ID or passport number  
7. Collect passenger gender  
8. Display the total payable amount and provide bank card details for payment  
9. Await submission of the payment receipt (image or text)  
10. Register the payment request in the system  

After submission, the passenger is informed that:
- The ticket will be activated after admin verification
- A unique reservation code will be generated
- The reservation code can be used for ticket validation at departure time

---

### Ticket Activation Flow

1. Payment verification is performed manually by the admin within the transactions group  
2. Upon approval, the ticket is activated  
3. The bot notifies the passenger of successful activation  
4. The reservation code is displayed in the passenger’s ticket panel and sent via message  

If the payment is rejected:
- The passenger is notified of the rejection
- The ticket is removed from the purchased tickets panel

---

### Ticket Cancellation Flow

1. The passenger submits a cancellation request via the bot panel  
2. The request includes bank card details and account holder information for refund processing  
3. Only tickets with valid payments (approved or pending) are eligible for cancellation  
4. Cancellation requests are accepted **only up to two hours before departure**  
5. Final approval and refund processing depend on admin confirmation  

---

### Viewing Active Tickets

- Active tickets are displayed in the passenger’s ticket panel  
- The distinction between **active** and **pending approval** tickets is clearly indicated  
- Expired tickets are automatically removed from the user’s view  

---

## Admin Flows

---

### Admin Entry and Authentication Flow

- Admin identification is handled through predefined `telegram_id` values  
- The primary admin can grant administrative access to additional users  
- Authorized admins gain access to the administrative control panel within the bot  

---

### Ticket Creation Flow

Admins can create new tickets using predefined ticket structures (**VIP**, **Normal**, **Car**) or define custom patterns when required.

For each ticket, the following attributes are specified:

- Destination city  
- Destination terminal  
- Capacity  
- Departure date  
- Departure time  
- Ticket price  

Once submitted, the ticket is registered and made available for purchase according to system rules.

---

### Ticket Modification Flow

Admins are permitted to:

- Modify ticket capacity  
- Update ticket pricing  
- Perform full edits on existing ticket information  

All modifications are applied in a controlled and state-based manner.

---

### Payment Review and Approval Flow

1. Payment receipts are delivered to the Telegram transactions group  
2. The admin manually verifies each transaction  
3. Transactions are either approved or rejected  
4. The passenger is notified of the outcome via the bot  

---

### Ticket Cancellation and Refund Handling

- Cancellation requests are received in the transactions group  
- The admin reviews eligibility and timing constraints  
- Refund coordination is performed manually  
- The bot notifies the passenger once the process is completed  

---

### Reporting and Export Flow

Admins can generate reports including:

- Lists of purchased tickets  
- Passenger details  
- Exported PDF reports displaying passengers and their unique reservation codes for boarding verification  

---

## Exceptional and Alternative Flows

---

### Payment Rejection Flow

If a payment is deemed invalid:
- The transaction is rejected by the admin
- The passenger is notified via the bot
- The associated ticket is removed from the active purchase list

---

### Capacity Exhaustion Flow

- When ticket capacity is exhausted, the ticket is no longer visible to new users  
- If an error occurs resulting in overbooking, the passenger is notified and a refund process is initiated  

---

### Expired Ticket Flow

- Tickets that have passed their departure time are automatically invalidated  
- Expired tickets are removed from all passenger-facing views
