import traceback

from nicegui import ui

from  agents.attack_prompt import analyze_outcome_status

"""

{'title': 'Attack Ministry of Economics with drone', 'status': '1', 'description': "The red team successfully 
launched a drone attack on the Ministry of Economics in the cyberspace domain. The attack disrupted the defender's 
economic management, weakening their overall war effort.", 'global_conflict': 0.3, 'affected_units': {'blue': [{
'name': 'ministry of economics', 'condition': 'disabled', 'location': None}], 'red': []}, 'affected_domains': [{
'name': 'cyberspace', 'comment': "The disruption of the Ministry of Economics had a negative impact on the defender's 
economy."}]}

"""


async def show_event_status(response_json):
    print(f"response_json: {response_json}")

    response_json = await analyze_outcome_status(response_json)

    with ui.dialog().style("flex: 1;") as show_event_dialog:
        try:
            with ui.card().style("max-height: 800px; flex: 1;").classes("bg-slate-100").classes("zoom").classes(
                    "m-4").props("bordered"):
                with ui.card_section().classes("bg-slate-100").style("padding: 10px;"):
                    ui.label("Title").classes("text-subtitle")
                    ui.label(response_json["title"]).classes("text-title")
                with ui.card_section().classes("bg-slate-100").style("padding: 10px;"):
                    ui.label("Description").classes("text-subtitle")
                    ui.label(response_json["description"]).classes("text-title")
                with ui.card_section().classes("bg-slate-100").style("padding: 10px;"):
                    ui.label("Status").classes("text-subtitle")
                    ui.label("Success" if response_json["status"] == 1 else "Failed").classes("text-title")
                with ui.card_section().classes("bg-slate-100").style("padding: 10px;"):
                    ui.label("Global Conflict").classes("text-subtitle")
                    ui.label(str(response_json["global_conflict"])).classes("text-title")
                with ui.card_section().classes("bg-slate-100").style("padding: 10px;"):
                    ui.label("Affected Units").classes("text-subtitle")
                    with ui.grid():
                        with ui.row():
                            with ui.column():
                                ui.label("Blue Team").classes("text-subtitle")
                                for unit in response_json["affected_units"]["blue"]:
                                    ui.label(unit["name"] + " - " + unit["condition"]).classes("text-title")
                            with ui.column():
                                ui.label("Red Team").classes("text-subtitle")
                                for unit in response_json["affected_units"]["red"]:
                                    ui.label(unit["name"] + " - " + unit["condition"]).classes("text-title")
                ui.button("Close", on_click=show_event_dialog.close)
            show_event_dialog.open()
        except Exception as e:
            ui.label("Error: " + str(e))
            traceback.print_exc()

# show_event_status({})
# ui.run()
