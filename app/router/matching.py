import os
import shutil
import PyPDF2, pdfplumber
import filetype
import time
from starlette.responses import JSONResponse
from app.celery_worker import create_task
from starlette import status
from fastapi import APIRouter, FastAPI, File, UploadFile, Body
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from app.utils import raise_pdf_not_valid, send_email, codeGenerate




router = APIRouter(
    prefix="/matching",
    tags=["Matching "],
    responses={404: {"description": "Not found"}}
)


# @router.post(bind=True)
# def long_task(self, iteration):
#     for i in range(1, iteration):
#         time.sleep(1)
#         self.update_state(state='PROGRESS',
#                           meta={'current': i, 'total': iteration,
#                                 'status': str(i) + '%'})
#     return {'current': 100, 'total': 100, 'status': '100%'}
# @router.post("/tasks", status_code=201)
# def run_task(payload = Body(...)):
#     task_type = payload["type"]
#     task = create_task.delay(int(task_type))
#     return JSONResponse({"task_id": task.id})

@router.post("/tasks")
def run_task(data=Body(...)):
    amount = int(data["amount"])
    x = data["x"]
    y = data["y"]
    task = create_task.delay(amount, x, y)
    return JSONResponse({"Result": task.get()})


@router.post("/uploadfile/")
async def upload_file(file: UploadFile=File(description="A file must be PDF")):
    src_dir = os.getcwd()
    if not file.content_type == 'application/pdf':
        raise raise_pdf_not_valid()

    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    old_file = src_dir +'/' + file.filename
    data_code = codeGenerate()
    dest_file = src_dir + "/static/files/" + f"{data_code}.pdf"
    shutil.move(old_file, dest_file)
    return JSONResponse(
        status_code=200,
        content={"message": f"File Successfully Upload"
                            f" id: {data_code}"}
    )


@router.post("/convert_compare/")
async def convert_comapare_data(id:str,  job_description: str):
    src_dir = os.getcwd()
    dest_file = src_dir + "/static/files/" + f"{id}.pdf"

    CV_File=open(dest_file,'rb')
    Script=PyPDF2.PdfFileReader(CV_File)
    pages=Script.numPages

    Script = []
    with pdfplumber.open(CV_File) as pdf:
        for i in range (0,pages):
            page=pdf.pages[i]
            text=page.extract_text()
            
            Script.append(text)

    Script=''.join(Script)
    uploaded_file_clear=Script.replace("\n","")
    
    Script_Req=''.join(job_description)
    job_description_clear=Script_Req.replace("\n","")

    matching_test=[uploaded_file_clear,job_description_clear]
    cv=CountVectorizer()
    count_matrix=cv.fit_transform(matching_test)

    match_percentage=cosine_similarity(count_matrix)[0][1]*100
    match_percentage=round(match_percentage,2)
    
    return JSONResponse(
        status_code=200,
        content={"message": str(match_percentage)+'% to Requirement'}
    )