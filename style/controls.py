import flet as ft


class MyContainer(ft.Container):
    def __init__(self, *args, opacity=0.07, **kwargs):
        super().__init__(*args, **kwargs)
        self.bgcolor = ft.colors.with_opacity(opacity=opacity, color="white")
        self.padding = ft.padding.symmetric(vertical=10, horizontal=30)
        self.border_radius = 12


class MyButton(ft.ElevatedButton):
    def __init__(
        self,
        *args,
        padding=ft.padding.symmetric(horizontal=35, vertical=23),
        text_size=19,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.style = ft.ButtonStyle(
            text_style=ft.TextStyle(size=text_size),
            padding=padding,
        )


class MyText(ft.Text):
    def __init__(self, *args, size=17, text_align=ft.TextAlign.CENTER, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = size
        if text_align == "L":
            self.text_align == ft.TextAlign.LEFT
        elif text_align == "R":
            self.text_align == ft.TextAlign.RIGHT
        elif text_align == "C":
            self.text_align == ft.TextAlign.CENTER
        else:
            self.text_align = text_align


class MyTextField(ft.TextField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bgcolor = ft.colors.with_opacity(1, "#191C20")
        self.border_radius = 10
        self.border_color = ft.colors.TRANSPARENT


class MyDropdown(ft.Dropdown):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bgcolor = ft.colors.with_opacity(1, "#191C20")
        self.border_radius = 10
        self.border_color = ft.colors.with_opacity(0.05, "white")
