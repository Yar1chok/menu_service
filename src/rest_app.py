
from src.app.custom_app import CustomApp
from src.routers.menu_router import menu_router


app = CustomApp(
    title="MenuService"
)

app.include_router(
    menu_router
)
