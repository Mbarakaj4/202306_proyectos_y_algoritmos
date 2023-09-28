# TODO List in Django

**Step 1** - *Create Kitty and make initial configs*\
Proceed like it's explained in the notes.md file

**Step 2** - *Create the dashboard views in kitten_1 app*\
You will need the following things:
1. Login and Register view, ensure that only empty session users access this page.
2. Dashboard view, to show:
    - Jobs; Device Cost Description Status JobNumber.
    - Reports; Type Description.
    - Clients; FirstName LastName PhoneNumber Description.
3. Jobs view, to show:
    - Queue; JobNumber Device Description Status.
    - Pending; JobNumber Device Description Status.
    - Ready; JobNumber Device Description Status.
    - Cancelled; JobNumber Device Description Status. 

**Step 3** - *Create databases*\
You will need to parse in Django ORM the next information
```
kitty_DB
    |- jobs
    |   |- id
    |   |- job_number
    |   |- device
    |   |- cost (default is 0)
    |   |- description(max 255)
    |   |- status_id
    |- status
    |   |- id
    |   |- types
    |- reports
    |   |- id
    |   |- type
    |   |- description(max 255)
    |- clients
    |   |- id
    |   |- first_name
    |   |- last_name
    |   |- phone_number
    |   |- description

telegram_bot
    |- welcome_text
    |   |- id
    |   |- text
    |- options
        |- id
        |- text

```
**Step 4** - *Create API endpoints*
