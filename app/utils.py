import os
import uuid
import smtplib
from fastapi import HTTPException
from dotenv import load_dotenv
load_dotenv(".env")

# Exceptions 
def raise_item_cannot_be_found_exception():
    return HTTPException(status_code=404,
                         detail="Data not found",
                         headers={"X-Header_Error":
                                  "Nothing to be seen at the UUID"})
# Exceptions 

def raise_pdf_not_valid():
    return HTTPException(status_code=500,
                         detail="File is not a PDF",
                         headers={"X-Header_Error":
                                  "Invalid Format"})


def send_email(send_to=str, message=str):
    sending_email = smtplib.SMTP('smtp.gmail.com', 587)
    sending_email.starttls()
    sending_email.login(os.environ.get("DEFAULT_EMAIL_SENDER"), os.environ.get("DEFAULT_EMAIL_SENDER_PASS"))
    sending_email.sendmail(os.environ.get("DEFAULT_EMAIL_SENDER"), send_to, message)
    # (subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
    sending_email.quit()


def codeGenerate():
	return f'{uuid.uuid4()}'
