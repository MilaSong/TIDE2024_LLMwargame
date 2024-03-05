from nicegui import ui


def dashboard():
    with ui.header().classes(replace='row items-center') as header:
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')

    with ui.left_drawer().classes('bg-blue-100').props('width=170') as left_drawer:
        ui.button('New game', on_click=lambda: ui.open("/new_game"), icon='settings').props('flat color=blue')
        ui.button('Wargame', on_click=lambda: ui.open("/"), icon='sports').props(
            'flat color=blue').classes(
            'justify-between')
        ui.button('Config', on_click=lambda: ui.open("/config"), icon='settings').props('flat color=blue')
