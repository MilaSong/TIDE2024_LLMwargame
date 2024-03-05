# import asyncio
#
# from nicegui import ui
#
# from app.agents.get_actions import get_actions
# from app.gameplay.game_state import GameState
#
# moving_team = GameState.get_next()
#
# select_list = GameState.get_team_units_str(moving_team)
# select_list = sorted(select_list, key=lambda x: x[0])
#
# target_list = GameState.get_team_units_str(GameState.get_opponent(moving_team))
# target_list = sorted(target_list, key=lambda x: x[0])
#
# selected = {
#     "attacker": "",
#     "target": ""
# }
#
#
# def str_to_unit(unit_str):
#     unit_list = unit_str.split("_")
#     # air_drone_working_Brest
#     if len(unit_list) == 3:
#         return {
#             "domain": unit_list[0],
#             "name": unit_list[1],
#             "condition": unit_list[2],
#             "location": None
#         }
#     else:
#         return {
#             "domain": unit_list[0],
#             "name": unit_list[1],
#             "condition": unit_list[2],
#             "location": unit_list[3]
#         }
#
#
# def generate_cards(response_json):
#     json_cards = response_json['results']
#     print(f"json_cards: {json_cards}")
#     with ui.dialog().style("flex: 1;") as card_dialog:
#         card_dialog.open()
#
#         for card in json_cards:
#             try:
#                 with ui.card().style("max-height: 500px; flex: 1;").classes("bg-slate-100").classes("zoom").classes(
#                         "m-4").props("bordered") as card_element:
#                     with ui.card_section().classes("bg-slate-100").style("padding: 10px;"):
#                         ui.label(card['title']).classes("text-h6"),
#                         ui.label("Description").classes("text-subtitle"),
#                         ui.label(card['description']),
#
#                         ui.label("Posibile outcome").classes("text-subtitle"),
#                         ui.label(card['outcome']),
#
#                         ui.label("Escalation to global conflict").classes("text-subtitle"),
#                         ui.label(card['escalation']),
#
#                         ui.label("Probability of success").classes("text-subtitle"),
#                         ui.label(card['probability']),
#
#                     ui.button("Select").style("margin-top: 10px;").classes(
#                         'w-full')
#             except Exception as e:
#                 print(f"Error: {e}")
#         print(f"card_dialog: {card_dialog}")
#
#         card_dialog.open()
#         card_dialog.open()
#         card_dialog.open()
#         card_dialog.open()
#
#
# async def generate_actions(old_dialog):
#     global selected
#
#     print("selected", selected)
#
#     with ui.dialog() as gen_action_dialog:
#         ui.spinner(size='lg')
#         ui.label('Generating actions')
#     gen_action_dialog.open()
#
#     attacker = str_to_unit(selected['attacker'])
#     target = str_to_unit(selected['target'])
#
#     response = await get_actions(attacker, target, "20km")
#     old_dialog.close()
#     gen_action_dialog.close()
#     print(f"response: {response}")
#     ui.notify('Asynchronous task finished')
#     generate_cards(response)
#
#
# async def selected_action(action):
#     ui.notify(f'Action selected: {action}')
#     with ui.dialog() as action_dialog:
#         ui.spinner(size='lg')
#         ui.label('Generating actions')
#     action_dialog.open()
#     await asyncio.sleep(1)
#     action_dialog.close()
#
#
# def show_new_move_dialog():
#     global selected
#     with ui.dialog() as new_move_dialog:
#         with ui.stepper().props('vertical').style('max-width: 600px; width: 50%') as stepper:
#             with ui.step('Select a unit').classes('w-full'):
#                 ui.label('Select a unit from the list or enter a custom')
#                 with ui.stepper_navigation().classes('w-full'):
#                     ui.select(options=select_list, new_value_mode='add', label='Select unit').classes(
#                         'w-full').bind_value_to(selected, 'attacker')
#                     ui.button('Next', on_click=stepper.next).classes('w-full')
#             with ui.step('Select a target').classes('w-full'):
#                 ui.label('Select a target from the list or enter a custom')
#                 with ui.stepper_navigation().classes('w-full'):
#                     ui.select(options=target_list, new_value_mode='add', label='Select target').classes(
#                         'w-full').bind_value_to(selected, 'target')
#                     ui.button('Back', on_click=stepper.previous).props('flat').classes('w-full')
#                     ui.button('Next', on_click=stepper.next).classes('w-full')
#             with ui.step('Confirm actions').classes('w-full'):
#                 ui.label('Review the actions and confirm')
#                 with ui.stepper_navigation().classes('w-full'):
#                     ui.button('Back', on_click=stepper.previous).props('flat').classes('w-full')
#                     ui.button('Generate actions', on_click=lambda x: generate_actions(new_move_dialog)).classes(
#                         'w-full')
#         new_move_dialog.open()
#
#
# # if __name__ == '__main__':
# # json_obj = {'results': [{'title': 'Drone cyber attack on ministry of economics', 'description': "Send a drone to perform a cyber attack on the enemy's ministry of economics, aiming to disrupt their economy.", 'outcome': "If successful, the cyber attack could disable the enemy's banking system and weaken their economic stability.", 'probability': 0.7, 'escalation': 0.1}, {'title': 'Drone reconnaissance on ministry of economics', 'description': "Send a drone to gather information on the enemy's ministry of economics, obtaining valuable intelligence.", 'outcome': "Successful reconnaissance could provide insight into the enemy's economic strategies and vulnerabilities.", 'probability': 0.8, 'escalation': 0.05}, {'title': 'Drone sabotage mission on enemy data center', 'description': "Deploy a drone to carry out a sabotagemission targeting the enemy's data center, aiming to disrupt their communication and data storage capabilities.", 'outcome': "If successful, the drone could disable the enemy's data center, hampering their military operations.", 'probability': 0.6, 'escalation': 0.2}, {'title': 'Drone surveillance on enemy drone base', 'description': 'Conduct surveillance using a drone to monitor enemy drone base, gathering intelligence on their capabilities and intentions.', 'outcome': "Successful surveillance could provide valuable information on the enemy's drone operations, allowing for better planning of future actions.", 'probability': 0.9, 'escalation': 0.05}, {'title': 'Drone strike on enemy drone', 'description': 'Launch a drone strike on an enemy drone located in Brest, aiming to eliminate their reconnaissance capabilities.', 'outcome': 'If successful, the drone strike could neutralize the enemy drone and limit their ability to gather information on our forces.', 'probability': 0.85, 'escalation': 0.1}]}
# # generate_cards(json_obj)
# # ui.run()
