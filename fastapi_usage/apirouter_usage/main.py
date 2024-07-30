from fastapi import FastAPI

import items
import apirouter_usage.users as users

# from fastapi_usage import items, users


app = FastAPI()
# 将路由分离到不同的模块中，保持代码的清晰和组织性。
app.include_router(items.router)
app.include_router(users.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=7860,
        log_level="debug",
        reload=True,
        loop="asyncio",
    )
