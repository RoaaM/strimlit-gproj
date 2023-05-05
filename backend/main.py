# from fastapi import FastAPI
 
# from app import __init__ as backend_app

# app = FastAPI()
# app.mount("/api", backend_app)

from fastapi import FastAPI
 
# from app import __init__ as backend_app
from routers.user import router as user_router
from routers.graph import router as graph_router
from routers.image import router as image_router
from routers.text import router as text_router

app = FastAPI()
app.include_router(user_router, prefix='/users', tags=['users'])
app.include_router(graph_router, prefix='/graphs', tags=['graphs'])
app.include_router(image_router, prefix='/images', tags=['images'])
app.include_router(text_router, prefix='/texts', tags=['texts'] )

@app.get('/')
async def root():
    return {"app": "G-Project"}