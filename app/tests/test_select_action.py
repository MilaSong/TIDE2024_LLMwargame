import asyncio

from nicegui import ui, app

from gui.modal.event_status import show_event_status
from gui.modal.show_cards import generate_cards

input_data = {'title': 'Attack Ministry of Economics with drone', 'status': '1', 'description': "The red team successfully launched a drone attack on the Ministry of Economics in the cyberspace domain. The attack disrupted the defender's economic management, weakening their overall war effort.", 'global_conflict': 0.3, 'affected_units': {'blue': [{'name': 'ministry of economics', 'condition': 'disabled', 'location': None}], 'red': []}, 'affected_domains': [{'name': 'cyberspace', 'comment': "The disruption of the Ministry of Economics had a negative impact on the defender's economy."}]}

async def setup_async_operations():
    await show_event_status(input_data)


# Schedule the async function to run at startup
app.on_startup(setup_async_operations)

ui.run()
