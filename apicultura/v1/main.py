from fastapi import FastAPI

from apicultura.v1.endpoints import (
    authentication_endpoints,
    user_endpoints,
    task_endpoints,
)

app = FastAPI(
    title="CRUD - ToDo Application in FastAPI",
    summary="""Endpoints for User and Authentication services.""",
)


@app.get("/")
async def index():
    """Root endpoint"""

    return {"message": "APIcultura v1."}


app.include_router(user_endpoints.router)
app.include_router(authentication_endpoints.router)
app.include_router(task_endpoints.router)
