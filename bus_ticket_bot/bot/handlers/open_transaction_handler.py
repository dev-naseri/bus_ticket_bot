"""

Open Transaction State Handler

when this handler run?
    when a transaction_open state is in user record and user try to do unexpected behavior

Transaction State's (What every transaction have?) (every step):
    step 1: phone_number -> int with length = 10 (without zero)
    step 2: nationality -> iranian, other -> query
    step 3: national/passport serial number -> str (because passport first char like A135234324 or J132342341)
    step 4: full_name -> str
    step 5: payment -> photo/text

in simple way:
    this handler never start because user never leave without purchase.
    but this is too humble! users allways make things complicated for developers.

for any step make sure it gets the right data, it can take wrong data?
    yes when str is open user can give us 'Buy Tickets' for passport id!!!
    what a mess

"""