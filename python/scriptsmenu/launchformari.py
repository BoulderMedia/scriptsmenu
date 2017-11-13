import scriptsmenu
from .vendor.Qt import QtWidgets

def _mari_main_window():
    """Return Mari's main window"""
    mari_main_window = QtWidgets.QApplication.activeWindow()
    return mari_main_window


def _mari_main_menubar():
    """Retrieve the main menubar of the Mari window"""
    mari_window = _mari_main_window()
    menubar = [i for i in mari_window.children()
               if isinstance(i, QtWidgets.QMenuBar)]

    assert len(menubar) == 1, "Error, could not find menu bar!"
    return menubar[0]


def main(title="Scripts"):
    mari_main_bar = _mari_main_menubar()
    for mari_bar in mari_main_bar.children():
        if isinstance(mari_bar, scriptsmenu.ScriptsMenu):
            if mari_bar.title() == title:
                menu = mari_bar
                return menu

    menu = scriptsmenu.ScriptsMenu(title=title, parent=mari_main_bar)
    return menu