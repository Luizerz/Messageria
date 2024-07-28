import flet as ft
from Publicador import DataType

def main(page: ft.Page):
    sensorList = []
    def buttonClick(e):
        if input_text.value in sensorList:
            page.snack_bar.content = ft.Text("Já existe um sensor com esse ID")
            page.snack_bar.open = True
        else:
            sensorList.append(input_text.value)
            page.snack_bar.content = ft.Text("Seu sensor foi criado com sucesso!")
            page.snack_bar.open = True
        page.update()
        
    page.title = "Publicador"
    page.horizontal_alignment = "CENTER"
    page.snack_bar = ft.SnackBar(
        content=ft.Text("Seu sensor foi criado com sucesso!"),
        action="Ok!",
    )

    input_text = ft.TextField( label="ID", hint_text="Digite o ID do sensor")
    submit_button = ft.ElevatedButton(text="Criar sensor", on_click=buttonClick)
    range_slider = ft.RangeSlider(
        min=-100,
        max=100,
        start_value=0,
        divisions=200,
        end_value=100,
        inactive_color=ft.colors.GREEN_300,
        active_color=ft.colors.GREEN_700,
        overlay_color=ft.colors.GREEN_100,
        label='{value}',
        width=350
    )
    drop_down = ft.Dropdown(
        label="Tipo de dado",
        options=[
            ft.dropdown.Option(DataType.velocity.name),
            ft.dropdown.Option(DataType.umidity.name),
            ft.dropdown.Option(DataType.temperature.name, ref=DataType.temperature),
            ],
        )
        
    page.add(ft.Row([input_text, drop_down], alignment="Center"), ft.Row([range_slider, submit_button], alignment="Center"))
ft.app(main)
