import flet as ft

def main(page: ft.Page):
    page.title = "Seletor de Cores"
    page.padding = 20

    caixa_colorida = ft.Container(
        content=ft.Text(
            "Escolha uma cor!",
            color=ft.Colors.WHITE,
            size=18,
            text_align=ft.TextAlign.CENTER
        ),
        bgcolor=ft.Colors.GREY,
        width=380,
        height=100,
        border_radius=10,
        alignment=ft.alignment.center
    )

    def cor_selecionada(evento):
        cor_escolhida = evento.control.value

        cores_disponiveis = {
            "Azul": ft.Colors.BLUE,
            "Verde": ft.Colors.GREEN,
            "Vermelho": ft.Colors.RED,
            "Roxo": ft.Colors.PURPLE,
            "Laranja": ft.Colors.ORANGE,
            "Rosa": ft.Colors.PINK
        }

        caixa_colorida.bgcolor = cores_disponiveis.get(cor_escolhida, ft.Colors.GREY)
        caixa_colorida.content.value = f"Cor selecionada: {cor_escolhida}"
        page.update()

    seletor_cor = ft.Dropdown(
        label="Escolha uma cor",
        width=200,
        options=[
            ft.dropdown.Option("Azul"),
            ft.dropdown.Option("Verde"),
            ft.dropdown.Option("Vermelho"),
            ft.dropdown.Option("Roxo"),
            ft.dropdown.Option("Laranja"),
            ft.dropdown.Option("Rosa")
        ],
        on_change=cor_selecionada
    )

    page.add(
        ft.Text("Seletor de Cores", size=24, weight=ft.FontWeight.BOLD),
        seletor_cor,
        caixa_colorida
    )

ft.app(target=main)
