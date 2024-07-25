from flet_core import ListView
import flet as ft
from  routesevents import ROUTES
# from flet_map import FletMap



def close_click(e):
    e.page.window_close()


def change_theme(e):
    e.page.theme_mode = 'light' if e.page.theme_mode == 'dark' else 'dark'
    e.page.update()


def show_drawer(e):
    e.page.views[0].drawer = e.page.drawer
    e.page.update()
    e.page.views[0].drawer.open = True
    e.page.views[0].drawer.update()


def change_route(e):
    route = ROUTES[e.control.selected_index]
    e.page.go(route)
    print(route)

