from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field

class User(BaseModel):
    last_name: str
    first_name: str
    email: str
    is_active: bool