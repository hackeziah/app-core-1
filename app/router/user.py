from starlette import status
from fastapi import APIRouter
from app.repository.user import UserRepo
from app.base_model import User
from starlette.responses import JSONResponse


router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"description": "Not found"}}
)


@router.get("/users/")
async def get_all():
    _userList = await UserRepo.retrieve()
    return JSONResponse(
        status_code=200,
        content={"message": f"Success retrieve all data" ,
               'result':_userList
        },
        
    )


@router.post("/user/create")
async def create(user: User):
    await UserRepo.insert(user)
    return JSONResponse(
        status_code=200,
        content={"message": f"Success save data" }
    )



@router.get("/user/{id}")
async def get_id(id: str):
    _user = await UserRepo.retrieve_id(id)
    return JSONResponse(
            status_code=200,
            content={"message": f"Success retrieve one" ,
               'result':_user
            },
    )


@router.post("/user/update")
async def update(user: User):
    await UserRepo.update(user.id,user)
    return JSONResponse(
            status_code=200,
            content={"message": f"Success update data"},
    )


@router.delete("/user/{id}")
async def delete(id: str):
    await UserRepo.delete(id)
    return JSONResponse(
            status_code=200,
            content={"message": f"Success delete dataa"},
    )
