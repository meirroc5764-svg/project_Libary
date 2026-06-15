from fastapi import APIRouter,HTTPException
from pydantic import BaseModel

from database.member_db import Member

m = Member()

router = APIRouter()

class DataModel(BaseModel):
    name:str
    email:str
    is_active:bool = True


@router.get("/members",status_code=200)
def all_members():
    all_members = m.show_all()
    
    if not all_members:
        raise HTTPException(status_code=404, detail="no have members")
    
    return all_members

@router.get("/members/{id}",status_code=200)
def members_by_id(id):
    my_member = m.get_member_by_id(id)
    
    if not my_member:
        raise HTTPException(status_code=404,detail="not fuond a member")
    
    return my_member


@router.post("/members",status_code=201)
def create_member(data:DataModel):
    try:
        if not "@" in data.email:
            raise HTTPException(status_code=400, detail="email enter not good")
        
        new_dict = data.model_dump()
        
        new_man = m.create_members(new_dict) 
        
        return {"message":f"create new user:{new_man}"}
    except:
        raise HTTPException(status_code=422, detail="create new false")