import asyncio

from nicegui import ui, app

from gui.modal.show_cards import generate_cards

input_data = {'results': [{'title': 'Attack Ministry of Economics with drone',
                           'description': 'Send a drone to attack the Ministry of Economics in the cyberspace domain.',
                           'outcome': "If successful, the attack can disrupt the defender's economic management and potentially weaken their overall war effort.",
                           'probability': 0.7, 'escalation': 0.1},
                          {'title': 'Launch cyber attack on Ministry of Economics',
                           'description': 'Launch a cyber attack on the Ministry of Economics in the cyberspace domain.',
                           'outcome': "A successful cyber attack can disrupt the defender's economic management and potentially weaken their overall war effort.",
                           'probability': 0.8, 'escalation': 0.2}, {'title': 'Deploy drone for reconnaissance',
                                                                    'description': "Use the drone to gather intelligence on the defender's cyber infrastructure and capabilities.",
                                                                    'outcome': 'Successful reconnaissance can provide valuable information for future cyber attacks.',
                                                                    'probability': 0.9, 'escalation': 0.05},
                          {'title': "Sabotage enemy's data center",
                           'description': "Target the enemy's data center in the cyber domain to disrupt their data storage and processing capabilities.",
                           'outcome': "A successful sabotage can severely hamper the defender's cyber operations.",
                           'probability': 0.6, 'escalation': 0.2},
                          {'title': "Launch a virus attack on the defender's cyber network",
                           'description': "Deploy a virus in the defender's cyber network to disrupt their communication and data exchange capabilities.",
                           'outcome': "A successful virus attack can cripple the defender's cyber capabilities and disrupt their operations.",
                           'probability': 0.7, 'escalation': 0.1}]}


async def setup_async_operations():
    await generate_cards(input_data)


# Schedule the async function to run at startup
app.on_startup(setup_async_operations)

ui.run()
