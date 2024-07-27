import flet as ft
from Publicador import DataType

def main(page: ft.Page):
    page.title = "Publicador"
    page.horizontal_alignment = "CENTER"
    input_text = ft.TextField( label="ID", hint_text="Digite o ID do sensor")
    range_slider = ft.RangeSlider(
        min=-100,
        max=100,
        start_value=0,
        divisions=200,
        end_value=100,
        inactive_color=ft.colors.GREEN_300,
        active_color=ft.colors.GREEN_700,
        overlay_color=ft.colors.GREEN_100,\
        label='{value}'
    )
    drop_down = ft.Dropdown(
        label="Tipo de dado",
        options=[
            ft.dropdown.Option(DataType.velocity.name),
            ft.dropdown.Option(DataType.umidity.name),
            ft.dropdown.Option(DataType.temperature.name, ref=DataType.temperature),
            ],
        )
    page.add(input_text, drop_down, range_slider)
ft.app(main)
