from nicegui import ui


def show_loading_dialog():
    with ui.dialog() as gen_action_dialog:
        ui.spinner(size='lg')
        ui.label('Generating actions')
    gen_action_dialog.open()
    return gen_action_dialog
