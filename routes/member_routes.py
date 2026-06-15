from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from database.db_connection import logger

from database.member_db import Member

m = Member()

router = APIRouter()

class DataModel(BaseModel):
    name:str
    email:str
    is_active:bool = True

class UpDataModel(BaseModel):
    name:str|None = None
    email:str| None = None
    is_active:bool | None = None


@router.get("/members",status_code=200)
def all_members():
    logger.info("take all member...")
    all_members = m.show_all()
    
    if not all_members:
        logger.error("not found a data")
        raise HTTPException(status_code=404, detail="no have members")
    logger.info("return all member to user")
    return all_members

@router.get("/members/{id}",status_code=200)
def members_by_id(id:int):
    logger.info("searches member by ID...")
    my_member = m.get_member_by_id(id)
    
    if not my_member:
        logger.error("not found a member by id")
        raise HTTPException(status_code=404,detail="not fuond a member")
    logger.info("return member from user")
    return my_member


@router.post("/members",status_code=201)
def create_member(data:DataModel):
    try:
        logger.info("cheak if user value valibol")
        if not "@" in data.email:
            logger.error("value not valibol")
            raise HTTPException(status_code=400, detail="email enter not good")
        
        new_dict = data.model_dump()
        logger.info("start create a member...")
        new_man = m.create_members(new_dict) 
        logger.info("create member successfully")
        return {"message":f"create new user:{new_man}"}
    except:

        raise HTTPException(status_code=422, detail="create new false")

@router.put("/member/{id}", status_code=200)
def change_member_by_id(id:int,data:UpDataModel):
    new_dict = data.model_dump(exclude_none=True)
    logger.info("start chenge a data by id")
    new_up = m.change_by_id(id,new_dict)
    if not new_up:
        logger.error("not found a data by id")
        raise HTTPException(status_code=404, detail=f"not faund a member with this id{id}")
    logger.info("change data finish successfully")
    return {"message":"update a member finish"}


@router.put("/member/{id}/deactivate", status_code=200)
def diactivate_member_by_id(id:int):
    logger.info("start diactivate a member...")
    member = m.diactivate_by_id(id)
    if not member:
        logger.info("not found a member from diactivate")
        raise HTTPException(status_code=404, detail=f"not faund a member with this id:{id}")
    logger.info("diactivate a member")
    return {"message":f"diactivate a member id:{id} finish"}


@router.put("/member/{id}/activate", status_code=200)
def activate_member_by_id(id:int):
    logger.info("start activate a member...")
    member = m.activate_by_id(id)
    if not member:
        logger.info("not found a member from activate")
        raise HTTPException(status_code=404, detail=f"not faund a member with this id:{id}")
    logger.info("member activate")
    return {"message":f"activate a member id:{id} finish"}

