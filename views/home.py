import flet as ft
import datetime
import requests
from style.controls import *
from requests_data.models import URL, Request


def send_get_request(url):
    request_time = datetime.datetime.now()
    status_code = None
    error = None
    try:
        response = requests.get(url)
        status_code = response.status_code

    except requests.exceptions.RequestException as e:
        error = e

    # Write request data to db


class HomeView(ft.View):
    def __init__(self, page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.scroll = ft.ScrollMode.ALWAYS
        self.padding = ft.padding.symmetric(horizontal=30, vertical=45)

        add_btn = ft.FloatingActionButton(
            icon=ft.icons.ADD_ROUNDED,
            on_click=self.add_clicked,
            bgcolor=ft.colors.with_opacity(0.14, "white"),
        )

        urls_parameters = MyContainer(
            ft.ResponsiveRow(
                [
                    MyText(
                        "URL", text_align=ft.TextAlign.LEFT, col={"sm": 5, "xl": 7.3}
                    ),
                    MyText("Method", col={"sm": 1.5, "xl": 1}),
                    MyText("Time interval", col={"sm": 2.5, "xl": 1.6}),
                    MyText("Status", col={"sm": 2, "xl": 1.8}),
                ]
            ),
            opacity=0.12,
        )
        self.urls_controls_container = ft.Column()

        requests_parameters = MyContainer(
            ft.ResponsiveRow(
                [
                    MyText("Time", col=1.7),
                    MyText("URL", text_align="L", col=6),
                    MyText("Method", col=2),
                    MyText("Status code", col=2.3),
                ]
            ),
            opacity=0.12,
        )
        requests_controls = self.get_requests_controls()

        content = ft.ResponsiveRow(
            [
                ft.Column(
                    [
                        urls_parameters,
                        self.urls_controls_container,
                        add_btn,
                        requests_parameters,
                        ft.Column(requests_controls),
                    ],
                    col={"xl": 8, "sm": 11, "xs": 11},
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=30,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        self.controls = [content]
        self.update_data()

    def get_requests_controls(self):
        requests_controls = []
        for req in Request.objects.all():
            # control for request data
            req_control = MyContainer(
                ft.ResponsiveRow(
                    [
                        MyText(req.sent_at, col=2),
                        MyText(req.url, col=6),
                        MyText(req.request_method, col=2),
                        MyText(req.http_status_code, col=2),
                    ]
                )
            )
            requests_controls.append(req_control)
        if requests_controls:
            return requests_controls
        else:
            return [ft.Text("No requests were sent", size=18, opacity=0.7)]

    def get_urls_controls(self):
        urls_controls = []
        for url in URL.objects.all():
            status = "Active" if url.is_active else "Not active"
            # control for request data
            url_control = MyContainer(
                ft.ResponsiveRow(
                    [
                        MyText(
                            url.url,
                            text_align=ft.TextAlign.LEFT,
                            col={"sm": 5, "xl": 7.3},
                        ),
                        MyText(url.request_method, col={"sm": 1.5, "xl": 1}),
                        MyText(url.time_interval, col={"sm": 2.5, "xl": 1.6}),
                        MyText(status, col={"sm": 2, "xl": 1.8}),
                        ft.Container(
                            content=ft.Icon(
                                ft.icons.CANCEL_ROUNDED,
                                size=23,
                                color=ft.colors.with_opacity(0.5, "red"),
                            ),
                            col={"sm": 1, "xl": 0.3},
                            on_click=lambda e, url_id=url.id: self.delete_url(
                                e, url_id
                            ),
                        ),
                    ]
                )
            )
            urls_controls.append(url_control)
        if urls_controls:
            return urls_controls
        else:
            return [ft.Text("Add URLs to send requests to", size=18, opacity=0.7)]

    def add_clicked(self, e):
        self.url_field = MyTextField(label="URL", col=7)
        self.url_method_field = MyDropdown(
            label="Method",
            options=[
                ft.dropdown.Option("GET"),
            ],
            col=2.5,
            value="GET",
        )
        self.url_time_interval_field = MyDropdown(
            label="Time interval",
            options=[
                ft.dropdown.Option(text="15 sec", key="00:00:15"),
                ft.dropdown.Option(text="30 sec", key="00:00:30"),
                ft.dropdown.Option(text="1 min", key="00:01:00"),
                ft.dropdown.Option(text="5 min", key="00:05:00"),
                ft.dropdown.Option(text="10 min", key="00:10:00"),
            ],
            col=2.5,
            value="00:10:00",
        )
        self.url_dlg = ft.AlertDialog(
            content=ft.Column(
                [
                    ft.ResponsiveRow(
                        [
                            self.url_field,
                            self.url_method_field,
                            self.url_time_interval_field,
                        ]
                    ),
                    ft.Row(
                        [
                            MyButton(
                                "Close",
                                color="red",
                                on_click=lambda _: self.page.close(self.url_dlg),
                            ),
                            MyButton(
                                "Add",
                                on_click=self.save_url,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                height=120,
                width=700,
            ),
        )
        self.page.open(self.url_dlg)

    def save_url(self, e):
        if not self.url_field.value:
            self.url_field.error_text = "URL field cannot be empty"
            self.page.update()
        else:
            new_url = URL()
            new_url.url = self.url_field.value
            new_url.is_active = False
            new_url.time_interval = self.url_time_interval_field.value
            new_url.request_method = self.url_method_field.value
            new_url.save()
            self.page.close(self.url_dlg)
            self.update_data()

    def delete_url(self, e, url_id):
        url = URL.objects.get(id=url_id)
        url.delete()
        self.update_data()

    def update_data(self):
        self.urls_controls_container.controls = self.get_urls_controls()
        self.page.update()
