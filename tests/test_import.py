import pytest


def test_modern_menu_instantiation():
    from kivy_garden.modernmenu import ModernMenu
    menu = ModernMenu()
    assert menu.radius == 50
