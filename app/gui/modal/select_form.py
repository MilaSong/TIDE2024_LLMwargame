from nicegui import ui

from  gameplay.game_state import GameState
from  gui.modal import selected
from  gui.modal.action_modal import generate_actions


def show_new_move_dialog():
    moving_team = GameState.get_next()

    select_list = GameState.get_team_units_str(moving_team)
    select_list = sorted(select_list, key=lambda x: x[0])

    target_list = GameState.get_team_units_str(GameState.get_opponent(moving_team))
    target_list = sorted(target_list, key=lambda x: x[0])

    with ui.dialog() as new_move_dialog:
        new_move_dialog.open()

        with ui.stepper().props('vertical').style('max-width: 600px; width: 50%') as stepper:
            with ui.step('Select a unit').classes('w-full'):
                ui.label('Select a unit from the list or enter a custom')
                with ui.stepper_navigation().classes('w-full'):
                    ui.select(options=select_list, new_value_mode='add', label='Select unit').classes(
                        'w-full').bind_value_to(selected, 'attacker')
                    ui.button('Next', on_click=stepper.next).classes('w-full')
            with ui.step('Select a target').classes('w-full'):
                ui.label('Select a target from the list or enter a custom')
                with ui.stepper_navigation().classes('w-full'):
                    ui.select(options=target_list, new_value_mode='add', label='Select target').classes(
                        'w-full').bind_value_to(selected, 'target')
                    ui.button('Back', on_click=stepper.previous).props('flat').classes('w-full')
                    ui.button('Next', on_click=stepper.next).classes('w-full')
            with ui.step('Confirm actions').classes('w-full'):
                ui.label('Review the actions and confirm')
                with ui.stepper_navigation().classes('w-full'):
                    ui.button('Back', on_click=stepper.previous).props('flat').classes('w-full')
                    ui.button('Generate actions', on_click=lambda x: generate_actions(new_move_dialog)).classes(
                        'w-full')
