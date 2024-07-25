import flet as ft

def main(page: ft.Page):
    # Начальный размер шрифта
    font_size = 20

    # Функция для изменения размера шрифта
    def change_font_size(e):
        nonlocal font_size
        font_size += 2
        text.value = f"Размер шрифта: {font_size}px"
        text.style = ft.TextStyle(size=font_size)
        page.update()

    # Текстовый виджет
    text = ft.Text(f"Размер шрифта: {font_size}px", style=ft.TextStyle(size=font_size))

    # Кнопка для изменения размера шрифта
    button = ft.ElevatedButton("Увеличить шрифт", on_click=change_font_size)
    button2 = ft.ElevatedButton("Уменьшить шрифт", on_click=change_font_size)

    # Добавление виджетов на страницу
    page.add(text, button)
    def change_font_size(e):
        nonlocal font_size
        font_size -= 2
        text.value = f"Размер шрифта: {font_size}px"
        text.style = ft.TextStyle(size=font_size)
        page.update()
# Запуск приложения
ft.app(target=main)
