import smtplib
import os
from fastapi import HTTPException


# Exceptions 
def raise_item_cannot_be_found_exception():
    return HTTPException(status_code=404,
                         detail="Data not found",
                         headers={"X-Header_Error":
                                  "Nothing to be seen at the UUID"})
# Exceptions 


def send_email(send_to=str, message=str):
    sending_email = smtplib.SMTP('smtp.gmail.com', 587)
    sending_email.starttls()
    sending_email.login('applaminar3@gmail.com', 'fksjohksykdcddga')
    sending_email.sendmail('applaminar3@gmail.com', send_to, message)
    # (subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
    sending_email.quit()
