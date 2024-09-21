import os
import sys
import django

# Add the django project directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "requester_django"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "requester_django.settings")
django.setup()

import flet as ft
from views.home import HomeView


def main(page: ft.Page):
    def route_changed(e):
        print(e.route)
        if e.route == "/":
            page.views.append(HomeView(page))
        page.update()

    page.on_route_change = route_changed

    page.go("/")


ft.app(target=main)
