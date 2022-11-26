from starlette import status
from fastapi import APIRouter, BackgroundTasks
from app.utils import send_email


router = APIRouter(
    prefix="/emailer",
    tags=["Emailer"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/send-email")
async def sending_email(email: str, message: str, background_tasks: BackgroundTasks):
    # check valid mailer
    if email and message:
        message = 'Subject: {}\n\n{}'.format("MyEmailer", message)
        return {"message": "Sending Email"}
    return {"message": "Fail"}


