from fastapi import FastAPI

from apicultura.v1.endpoints import user_endpoints

app = FastAPI(
    title='CRUD - ToDo Application in FastAPI', summary=""""missing summary"""
)


@app.get('/')
async def index():
    """Root endpoint"""
    return {'message': 'APIcultura v1.'}


app.include_router(user_endpoints.router)
