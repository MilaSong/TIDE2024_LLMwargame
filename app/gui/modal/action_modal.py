from nicegui import ui

from  agents.get_actions import get_actions
from  gui.modal import selected, str_to_unit
from  gui.modal.loading import show_loading_dialog
from  gui.modal.show_cards import generate_cards


async def generate_actions(old_dialog):

    print("selected", selected)

    loading_dialog = show_loading_dialog()

    attacker = str_to_unit(selected['attacker'])
    target = str_to_unit(selected['target'])

    print(f"attacker: {attacker}")
    print(f"target: {target}")

    response = await get_actions(attacker, target, "20km")
    # old_dialog.close()
    # loading_dialog.close()
    print(f"response: {response}")
    ui.notify('Clleared all actions')
    # show_loading_dialog.close()
    await generate_cards(response)