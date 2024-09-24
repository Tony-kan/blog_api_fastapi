import uvicorn
from fastapi import FastAPI
from database import Base, engine
from core.user.routes import user_router
from core.post.routes import post_router

app = FastAPI(
    title="Blog App",
    description="Backend of the blog api",
    version="v1"
)

app.include_router(user_router, prefix="/users",tags=["AUTH"])
app.include_router(post_router,prefix="/posts",tags=["POSTS"])

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
