import flet as ft
from flet_route import Routing
from routes import app_routes
from models import *


def main(page: ft.Page):
    page.window.width = 500
    page.window.height = 900
    page.window.resizable = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    Routing(
        page=page,
        app_routes=app_routes,
    )

    page.go(page.route)
    page.update()


if __name__ == '__main__':
    try:
        db.connect()
        # db.create_tables([Museum])
        ft.app(target=main)
    except KeyboardInterrupt:
        db.close()
        exit(0)
