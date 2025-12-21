# 07 - Business Rules

## Overview
- Briefly explain why business rules exist: to ensure correct behavior of the bot, maintain data integrity, and enforce operational policies.
- Mention that rules apply to Buyers, Admins, Tickets, and Transactions.

---

## Buyer Rules
- Users must start the bot with `/start` and can access `/help` for instructions.
- Ticket purchase flow: `VIP/NORMAL/CAR -> Cities -> Days -> Hours -> Quantity -> Personal Info -> Payment`.
- Both active tickets (payment confirmed) and pending tickets (awaiting payment confirmation) are shown in the panel.
- Each user will be banned after **three invalid transactions or invalid receipt submissions**; access to the bot will be revoked.
- Users can request refunds up to **2 hours before the scheduled departure time**.  
  - A **20% fee** will be deducted from the refund amount.  
  - After 2 hours prior to departure, **refund requests are no longer allowed**.
- Users cannot buy more seats than available.

---

## Admin Rules
- Admins can add, edit, or delete tickets.
- Admins approve or reject refund requests.
- Admins can generate reports for ticket sales and transactions.
- Admins can issue warnings to users; 3 warnings result in a ban.
- All receipts must be stored in a Telegram group for record-keeping.
- Changes in ticket price or seats affect only future purchases.

---

## Ticket Rules
- Ticket price must be greater than 0.
- Ticket dates must be valid and in the future.
- Ticket hours must follow 24-hour format.
- Seat count must be at least 1.
- VIP, NORMAL, and CAR tickets may have different price and availability rules.

---

## Transaction Rules
- Each purchase generates a unique `transaction_id`.
- Payment must be verified via receipt before ticket activation.
- Refunds must reference a valid `transaction_id`.
- Partial refunds are allowed if permitted by admin policy.
- Tickets once activated cannot be changed except for refund or admin action.

---

## Optional: Notes
- Any future business rules (e.g., promotions, discounts, special events) should be documented here.
