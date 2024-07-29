import flet as ft
from Publicador import DataType, PublisherData

def main(page: ft.Page):
    sensorList = []
    def validade(e):
        if all([input_text.value, drop_down.value]):
            submit_button.disabled = False
        else:
            submit_button.disabled = True
        page.update()
            
    def buttonClick(e):
        if input_text.value in sensorList:
            page.snack_bar.content = ft.Text("Já existe um sensor com esse ID")
            page.snack_bar.open = True
        else:
            sensorList.append(input_text.value)
            PublisherData(drop_down.value, input_text.value, range_slider.start_value, range_slider.end_value)
            print(drop_down.value)
            page.snack_bar.content = ft.Text("Seu sensor foi criado com sucesso!")
            page.snack_bar.open = True
        page.update()
        
    page.title = "Publicador"
    page.horizontal_alignment = "CENTER"
    page.snack_bar = ft.SnackBar(
        content=ft.Text("Seu sensor foi criado com sucesso!"),
        action="Ok!",
    )
    page.window.width = 800
    page.window.height = 350
    page.window.resizable = False
    page.vertical_alignment = "CENTER"
    page.horizontal_alignment = "CENTER"
    page.theme = ft.Theme(color_scheme_seed=ft.colors.PURPLE_ACCENT_700)


    input_text = ft.TextField( label="ID", hint_text="Digite o ID do sensor", on_change=validade)
    submit_button = ft.ElevatedButton(text="Criar sensor", on_click=buttonClick)

    range_slider = ft.RangeSlider(
        min=-100,
        max=100,
        start_value=0,
        divisions=200,
        end_value=100,
        label='{value}',
        width=350,
    )
    drop_down = ft.Dropdown(
        label="Tipo de dado",
        options=[
            ft.dropdown.Option(DataType.velocity.value, text=DataType.velocity.value),
            ft.dropdown.Option(DataType.umidity.value, text=DataType.umidity.value),
            ft.dropdown.Option(DataType.temperature.value, text=DataType.temperature.value),
            ],
        )
    range_slider_label = ft.Text((str(range_slider.start_value) + " até " + str(range_slider.end_value)))
    def slider_label_change(e):
        range_slider_label.value = str(int(range_slider.start_value)) + " até " + str(int(range_slider.end_value))
        page.update()
    range_slider.on_change = slider_label_change
    
    submit_button.disabled = True
    input_text.on_change = validade
    drop_down.on_change = validade
    
    page.add(ft.Row([input_text, drop_down], alignment="Center"), ft.Row([range_slider, range_slider_label, submit_button], alignment="Center"))
ft.app(main)
