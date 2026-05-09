Title: How to fix Gmail's 405 error for emails sent from Django using mail_admins
Date: 2025-10-23 10:27
Modified: 2025-10-23 10:27
Tags: recipes, Python
Category: Python
Slug: django-mail-admins
Authors: aekazakov
Summary: Set SERVER_EMAIL = EMAIL_HOST_USER

Django has a convenience function for sending emails to the site admins, django.core.mail.mail_admins().

This function sends emails from the address specified in the EMAIL_HOST_USER setting.

The “From:” header of the email will be the value of the SERVER_EMAIL setting.

By default, the SERVER_EMAIL setting is 'root@localhost'.

If EMAIL_HOST_USER is a Gmail address, and the "From:" header of the email is different from the sender address, Gmail may return the 450 error with obscure message like:

```
'The user you are trying to contact is receiving mail at a rate that 
prevents additional messages from being delivered. Please resend your 
message at a later time. If the user is able to receive mail at that 
time, your message will be delivered. For more information, go to 
https://support.google.com/mail/?p=ReceivingRate'
```

To fix this error, add SERVER_EMAIL = EMAIL_HOST_USER to the settings.py file of your Django project after you set EMAIL_HOST_USER. 

It will put the sender address to the "From:" header of emails sent with the mail_admins() function.

