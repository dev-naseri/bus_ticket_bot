# Bus Transit System (Telegram-Based)

## Overview

This project aims to design and implement a Telegram-based ticket reservation system
for public transportation services, with a primary focus on small and local transport operators.

The system acts as a digital operator, enabling end-users to browse routes, reserve tickets,
and complete payments through a Telegram bot interface.

---

## Problem Description

In many small towns, bus ticket sales are still handled manually or through traditional methods.
This leads to passengers spending a lot of time, sometimes experiencing confusion, and
operators facing additional pressure and complexity.

The main problem is that **the process of online ticket reservation is not simple or reliable for users**
and often results in a slow and frustrating experience.

The Telegram-based bus ticket reservation bot should cover the following steps:

1. Ticket date, time, and capacity are defined by the admin.  
2. Passenger's full name, phone number, and national ID are collected.  
3. Ticket date and time are selected by the passenger (only two sessions per week, according to admin settings).  
4. Payment is made via card-to-card transfer.  
5. Final confirmation is done by the admin.  
6. Reservation is completed, and a reservation code is assigned to the passenger.  
7. The list of reservations with passenger details is available for the admin and can be exported.  
8. Passengers can cancel their reservation and receive a refund up to two hours before departure.

---

## Users / Stakeholders

The primary users of this system are **passengers with limited technical knowledge** who want
to reserve tickets quickly and without hassle.

Operators of small transport companies or local transit groups are also stakeholders and need
reservation and payment management to be **simple, manageable, and error-free**.

---

## Challenges / Constraints

- Tickets must be limited by day and time, and if the capacity is full, that time slot should not be available.  
- Only two sessions per week are available, and selection must follow admin settings.  
- Payments are card-to-card and require manual admin confirmation.  
- Ticket cancellations are allowed up to two hours before departure, with a partial refund.  
- Throughout the process, users should experience **minimal confusion and wasted time**.  
- Reservation lists and passenger information must be viewable and exportable by the admin.

---

## Value / Why It Matters

Solving this problem ensures that users:

- Can **reserve tickets confidently and with peace of mind**  
- Have a fast and simple booking experience  
- Operators can manage reservations and payments **effectively and with minimal effort**
