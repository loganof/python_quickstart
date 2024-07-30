from fastapi import APIRouter


router = APIRouter()


@router.get("/users/")
async def read_users():
    return [{"username": "user1"}, {"username": "user2"}]


@router.get("/users/{username}")
async def read_user(username: str):
    return {"username": username}
