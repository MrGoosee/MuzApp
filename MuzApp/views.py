import flet as ft
import flet.map as map
from flet_route import Params, Basket

from events import close_click, change_theme, show_drawer, change_route
from models import Museum, Events, MapCoordinates


def indexView(page: ft.Page, params: Params, basket: Basket):
    museums = Museum.select()
    page.drawer = ft.NavigationDrawer(
        selected_index=-1,
        on_change=change_route,
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="О приложении",
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                label="О городе",
            ),
            ft.NavigationDrawerDestination(
                label="События",
            ),
        ],
    )
    return ft.View(
        "/",
        [
            ft.AppBar(
                leading=ft.IconButton(ft.icons.MUSEUM, on_click=show_drawer),
                leading_width=40,
                title=ft.Text("Музеи"),
                center_title=False,
                bgcolor=ft.colors.SURFACE_VARIANT, actions=[
                    ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=change_theme),
                    ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(
                                "Настройки", on_click=lambda _: page.go('/settings/')
                            ),
                            ft.PopupMenuItem(
                                text="Поддержка", on_click=lambda _: page.go('/support/')
                            ),
                            ft.PopupMenuItem(
                                text="Выйти", on_click=close_click
                            ),
                        ]
                    ),
                ],
            ),
            ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Image(
                                    height=80,
                                    width=80,
                                    src=item.image,
                                    fit=ft.ImageFit.CONTAIN,
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Text(item.title),
                                        ft.ElevatedButton('Смотреть подробнее',
                                                          on_click=lambda _, item_id=item.id: page.go(
                                                              f"/mus/{item_id}")),
                                    ]
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START
                        ),
                    ) for item in museums
                ],
            ),
        ],
        scroll=ft.ScrollMode.ALWAYS,
    )


def museumInfoView(page: ft.Page, params: Params, basket: Basket):
    id = int(params.get('id'))
    museum = Museum.get_by_id(id)
    mapcoordin = MapCoordinates.get_by_id(id)
    return ft.View(
        "/mus/:id",
        controls=[
            ft.AppBar(
                leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/")),
                leading_width=40,
                title=ft.Text(museum.title),
                center_title=False,
                bgcolor=ft.colors.SURFACE_VARIANT,
                actions=[
                    ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=change_theme),
                    ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(
                                text="Настройки", on_click=lambda _: page.go('/settings/')
                            ),
                            ft.PopupMenuItem(
                                text="Поддержка", on_click=lambda _: page.go('/support/')
                            ),
                            ft.PopupMenuItem(
                                text="Выйти", on_click=close_click
                            ),
                        ]
                    ),
                ],
            ),
            ft.Column(
                controls=[
                    ft.Image(
                        height=400,
                        width=400,
                        src=museum.image,
                        fit=ft.ImageFit.FIT_WIDTH
                    ),
                    ft.Text(museum.description),
                ],
            ),
            ft.Column(
                controls=[
                    ft.Text(museum.contacts),
                    ft.Text(museum.address),
                    ft.Text(museum.work_time),
                    ft.Text(museum.website),
                    map.Map(
                        width=500,
                        height=200,
                        configuration=map.MapConfiguration(
                            initial_center=map.MapLatitudeLongitude(mapcoordin.longitude, mapcoordin.latitude),
                            initial_zoom=19.0,
                            interaction_configuration=map.MapInteractionConfiguration(
                                flags=map.MapInteractiveFlag.ALL
                            ),
                        ),
                        layers=[
                            map.TileLayer(
                                url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                                on_image_error=lambda e: print("TileLayer Error"),
                            ),
                            map.MarkerLayer(
                                markers=[
                                    map.Marker(
                                        content=ft.Icon(ft.icons.LOCATION_ON, color=ft.cupertino_colors.DESTRUCTIVE_RED),
                                        coordinates=map.MapLatitudeLongitude(mapcoordin.longitude, mapcoordin.latitude),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],

            ),
            ft.ElevatedButton("Назад", on_click=lambda _: page.go("/")),
        ],
        scroll=ft.ScrollMode.ALWAYS
    )


def aboutAppView(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        '/about_app/',
        [
            ft.AppBar(
                leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/")),
                leading_width=40,
                title=ft.Text('О приложении'),
                center_title=False,
                bgcolor=ft.colors.SURFACE_VARIANT,
                actions=[
                    ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=change_theme),
                    ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(
                                text="Настройки", on_click=lambda _: page.go('/settings/')
                            ),
                            ft.PopupMenuItem(
                                text="Поддержка", on_click=lambda _: page.go('/support/')
                            ),
                            ft.PopupMenuItem(
                                text="Выйти", on_click=close_click
                            ),
                        ]
                    ),
                ],
            ),
            ft.Column(
                controls=[
                    ft.Text(
                        'Разрабатываемое мобильное приложение "Музеи Ульяновской области" предназначено для популяризации '
                        'культурного наследия региона и улучшения взаимодействия посетителей с музеями.'
                        ' Приложение предоставляет пользователям удобный доступ к информации о музеях, событиях и выставках,'
                        ' а также предлагает ряд полезных функций для планирования и организации посещений.'
                    )
                ],
            ),
            ft.ElevatedButton("Назад", on_click=lambda _: page.go("/")),
        ],
        scroll=ft.ScrollMode.ALWAYS

    )


def aboutAppCity(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        '/about_city/',
        [
            ft.AppBar(
                leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/")),
                leading_width=40,
                title=ft.Text('О городе'),
                center_title=False,
                bgcolor=ft.colors.SURFACE_VARIANT,
                actions=[
                    ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=change_theme),
                    ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(
                                text="Настройки", on_click=lambda _: page.go('/settings/')
                            ),
                            ft.PopupMenuItem(
                                text="Поддержка", on_click=lambda _: page.go('/support/')
                            ),
                            ft.PopupMenuItem(
                                text="Выйти", on_click=close_click
                            ),
                        ]
                    ),
                ],
            ),
            ft.Column(
                controls=[
                    ft.Image(
                        height=300,
                        width=600,
                        src='img/scale_1200.jpg',
                        fit=ft.ImageFit.FIT_WIDTH
                    ),
                    ft.Text(
                        'Ульяновск – это исторический и культурный центр Ульяновской области,'
                        ' расположенный на берегах реки Волги.'
                        'Город, основанный в 1648 году как крепость Синбирск, '
                        'богат своей многовековой историей и культурными традициями.'
                        'В 1924 году город был переименован в честь Владимира Ленина (Ульянова), который здесь родился.'
                    ),

                ],
            ),
            ft.ElevatedButton("Назад", on_click=lambda _: page.go("/")),
        ],
        scroll=ft.ScrollMode.ALWAYS

    )


def settings(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        '/settings/',
        [
            ft.AppBar(
                leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/")),
                leading_width=40,
                title=ft.Text('Настройки'),
                center_title=False,
                bgcolor=ft.colors.SURFACE_VARIANT,
                actions=[
                    ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=change_theme),
                    ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(
                                text="Настройки", on_click=lambda _: page.go('/settings/')
                            ),
                            ft.PopupMenuItem(
                                text="Поддержка", on_click=lambda _: page.go('/support/')
                            ),
                            ft.PopupMenuItem(
                                text="Выйти", on_click=close_click
                            ),
                        ]
                    ),
                ],
            ),
            ft.Column(
                controls=[

                ],
            ),
            ft.ElevatedButton("Назад", on_click=lambda _: page.go("/")),
        ],
        scroll=ft.ScrollMode.ALWAYS
    )


def supportView(page: ft.Page, params: Params, basket: Basket):
    return ft.View(
        "/support/",
        [
            ft.AppBar(
                leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/")),
                leading_width=40,
                title=ft.Text("События"),
                center_title=False,
                bgcolor=ft.colors.SURFACE_VARIANT, actions=[
                    ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=change_theme),
                    ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(
                                "Настройки", on_click=lambda _: page.go('/settings/')
                            ),
                            ft.PopupMenuItem(
                                text="Поддержка", on_click=lambda _: page.go('/support/')
                            ),
                            ft.PopupMenuItem(
                                text="Выйти", on_click=close_click
                            ),
                        ]
                    ),
                ],
            ),
            ft.Column(
                controls=[
                    ft.Text('Для связи с нами напишите нам на почту: ulyanovsk-muz@yandex.ru'),
                    ft.ElevatedButton("Назад", on_click=lambda _: page.go("/")),
                ],
            ),
        ],
        scroll=ft.ScrollMode.ALWAYS,
    )


def allEventsViews(page: ft.Page, params: Params, basket: Basket):
    events = Events.select()

    return ft.View(
        "/events/",
        [
            ft.AppBar(
                leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/")),
                leading_width=40,
                title=ft.Text("События"),
                center_title=False,
                bgcolor=ft.colors.SURFACE_VARIANT, actions=[
                    ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=change_theme),
                    ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(
                                "Настройки", on_click=lambda _: page.go('/settings/')
                            ),
                            ft.PopupMenuItem(
                                text="Поддержка", on_click=...
                            ),
                            ft.PopupMenuItem(
                                text="Выйти", on_click=close_click
                            ),
                        ]
                    ),
                ],
            ),
            ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Image(
                                    height=80,
                                    width=80,
                                    src=item.image,
                                    fit=ft.ImageFit.CONTAIN,
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Text(item.title),
                                        ft.ElevatedButton('Смотреть подробнее',
                                                          on_click=lambda _, item_id=item.id: page.go(
                                                              f"/event/{item_id}")),
                                    ]
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START
                        ),
                    ) for item in events
                ],
            ),
        ],
        scroll=ft.ScrollMode.ALWAYS,
    )
def eventInfo(page: ft.Page, params, basket: Basket):
    id = int(params.get('id'))
    event = Events.get_by_id(id)
    return ft.View(
        "/event/:id",
        controls=[
            ft.AppBar(
                leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/events/")),
                leading_width=40,
                title=ft.Text(event.title),
                center_title=False,
                bgcolor=ft.colors.SURFACE_VARIANT,
                actions=[
                    ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=change_theme),
                    ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(
                                text="Настройки", on_click=lambda _: page.go('/settings/')
                            ),
                            ft.PopupMenuItem(
                                text="Поддержка", on_click=...
                            ),
                            ft.PopupMenuItem(
                                text="Выйти", on_click=close_click
                            ),
                        ]
                    ),
                ],
            ),
            ft.Column(
                controls=[
                    ft.Image(
                        height=400,
                        width=400,
                        src=event.image,
                        fit=ft.ImageFit.FIT_WIDTH
                    ),
                    ft.Text(event.description),
                ],
            ),

            ft.ElevatedButton("Назад", on_click=lambda _: page.go("/")),
        ],
        scroll=ft.ScrollMode.ALWAYS
    )