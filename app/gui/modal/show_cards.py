import traceback

from nicegui import ui

from gui.modal.event_status import show_event_status
from functools import partial

"""
{'results': [{'title': 'Attack Ministry of Economics with drone', 'description': 'Send a drone to attack the Ministry of Economics in the cyberspace domain.', 'outcome': "If successful, the attack can disrupt the defender's economic management and potentially weaken their overall war effort.", 'probability': 0.7, 'escalation': 0.1}, {'title': 'Launch cyber attack on Ministry of Economics', 'description': 'Launch a cyber attack on the Ministry of Economics in the cyberspace domain.', 'outcome': "A successful cyber attack can disrupt the defender's economic management and potentially weaken their overall war effort.", 'probability': 0.8, 'escalation': 0.2}, {'title': 'Deploy drone for reconnaissance', 'description': "Use the drone to gather intelligence on the defender's cyber infrastructure and capabilities.", 'outcome': 'Successful reconnaissance can provide valuable information for future cyber attacks.', 'probability': 0.9, 'escalation': 0.05}, {'title': "Sabotage enemy's data center", 'description': "Target the enemy's data center in the cyber domain to disrupt their data storage and processing capabilities.", 'outcome': "A successful sabotage can severely hamper the defender's cyber operations.", 'probability': 0.6, 'escalation': 0.2}, {'title': "Launch a virus attack on the defender's cyber network", 'description': "Deploy a virus in the defender's cyber network to disrupt their communication and data exchange capabilities.", 'outcome': "A successful virus attack can cripple the defender's cyber capabilities and disrupt their operations.", 'probability': 0.7, 'escalation': 0.1}]}
"""


async def generate_cards(response_json):
    json_cards = response_json['results']
    print(f"json_cards: {json_cards}")
    with ui.dialog().style("flex: 1;") as card_dialog:
        card_dialog.open()
        for card in json_cards:
            try:
                with ui.card().style("max-height: 550px; flex: 1;").classes("bg-slate-100").classes("zoom").classes(
                        "m-4").props("bordered") as card_element:
                    with ui.card_section().classes("bg-slate-100").style("padding: 10px;"):
                        ui.label(card['title']).classes("text-h6"),
                        ui.label("Description").classes("text-subtitle"),
                        ui.label(card['description']),

                        ui.label("Posibile outcome").classes("text-subtitle"),
                        ui.label(card['outcome']),

                        ui.label("Escalation to global conflict").classes("text-subtitle"),
                        ui.label(card['escalation']),

                        ui.label("Probability of success").classes("text-subtitle"),
                        ui.label(card['probability']),
                    # show_event_status
                    ui.button("Select", on_click=partial(show_event_status, card)).classes('w-full')
                card_dialog.open()
            except Exception as e:
                print(f"Error: {e}")
                traceback.print_exc()
            card_dialog.open()
        card_dialog.open()

        print(f"card_dialog: {card_dialog}")
