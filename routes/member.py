from fastapi import APIRouter,HTTPException
from database import user_collection 
from models import create_members,update_members
from bson import ObjectId 

router = APIRouter()

def user_serializer(members) -> dict:
    return {
        "_id": str(members["_id"]),
        "name": members["name"],
        "year": members["year"],
        "dev": members["dev"],
        "des": members["des"],
        "pm": members["pm"],
        "core": members["core"],
        "mentor": members["mentor"],
        "major": members["major"],
        "minor": members["minor"],
        "birthday": members["birthday"],
        "home": members["home"],
        "quote": members["quote"],
        "favorite thing 1": members.get("favorite thing 1", "favorite_thing_1"),  
        "favorite thing 2": members.get("favorite thing 2", "favorite_thing_2"),
        "favorite thing 3": members.get("favorite thing 3", "favorite_thing_3"),
        "favorite dartmouth tradition": members.get("favorite dartmouth tradition", "favorite_dartmouth_tradition"),
        "fun fact": members.get("fun fact", "fun_fact"),
        "picture": members["picture"]
    }


@router.get("/members")
async def get_members():
    get_members =await user_collection.find().to_list(1000)
    return [user_serializer(member) for member in get_members]


@router.get("/members/{id}")
async def get_member(id:str):
    get_member =await user_collection.find_one({"_id":ObjectId(id)})
    return user_serializer(get_member)


@router.post("/members/create")
async def create_member(model:create_members):
    create_member = await user_collection.insert_one(model.dict(by_alias=True))
    find_member = await user_collection.find_one({"_id":create_member.inserted_id})
    if not find_member:
        raise HTTPException(status_code=404, detail="User cannot be created")
    else:
        return user_serializer(find_member) 

@router.put("/members/update/{id}")
async def update_member(id:str, model:update_members):
    update_member = await user_collection.update_one(
        {"_id":ObjectId(id)}, {"$set":model.dict(exclude_unset=True)} 
    )
    find_the_member = await user_collection.find_one( {"_id":ObjectId(id)})
    return user_serializer(find_the_member)


@router.delete("/members/delete/{id}")
async def delete_member(id:str):
    delete_member =await user_collection.delete_one({"_id":ObjectId(id)})
    if delete_member.deleted_count == 0:
        raise HTTPException(status_code=404, detail= " There is no member as such :( ")
    return {"message":f"User with id:{id} Successfully deleted !"}



