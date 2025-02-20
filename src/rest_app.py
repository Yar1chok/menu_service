

from fastapi import FastAPI

from src.routers.menu_router import menu_router


app = FastAPI()

app.include_router(
    menu_router
)
