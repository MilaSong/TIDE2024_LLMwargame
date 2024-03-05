from nicegui import ui

from gameplay.game_state import GameState
#from gui.upload_files import get_resource_data

# Json config files
redTeamCountries = ['XX', 'YY']
blueTeamCountries = [
    'Germany', 'United Kingdom', 'France', 'Italy', 'Spain', 'Poland', 'Ukraine',
    'Romania', 'Netherlands', 'Belgium', 'Sweden', 'Czech Republic (Czechia)', 'Greece',
    'Portugal', 'Hungary', 'Belarus', 'Austria', 'Switzerland', 'Serbia', 'Bulgaria', 'Denmark',
    'Slovakia', 'Finland', 'Norway', 'Ireland', 'Croatia', 'Moldova', 'Bosnia and Herzegovina',
    'Albania', 'Lithuania', 'Slovenia', 'North Macedonia', 'Latvia', 'Estonia', 'Luxembourg',
    'Montenegro', 'Malta', 'Iceland', 'Andorra', 'Liechtenstein', 'Monaco', 'San Marino', 'Holy See'
]

selected_values = {
    "red_countries": "",
    "blue_countries": ""
}

redTeamUnits = []
blueTeamUnits = []

units = []


def save_and_start_game():
    for team in selected_values["red_countries"]:
        GameState.append_team({
            "country": team,
            "name": "red"
            })
    for team in selected_values["blue_countries"]:
        GameState.append_team({
            "country": team,
            "name": "blue"
            })
    for unit in redTeamUnits:
        GameState.append_team_units({
            "name": unit["unit"],
            "condition": "working",
            "location": unit["where"]
        }, "red")
    for unit in blueTeamUnits:
        GameState.append_team_units({
            "name": unit["unit"],
            "condition": "working",
            "location": unit["where"]
        }, "blue")

    ui.open("/")


def new_game():
    ui.button("Start game", on_click=save_and_start_game).classes("mx-auto")
    with ui.row().classes('w-full p-0 flex-nowrap').style('gap: 0; margin-top: 10px'):
        with ui.card().style(
                'width: 50%; height: fit-content; min-height: 200px; align-items: center; margin-right: 20px;'):
            with ui.element('div').classes('mt-2 py-2 px-8 bg-red-600 rounded-lg'):
                ui.label('Red Team').classes('text-white')
            with ui.stepper().props('vertical').classes('w-full') as stepper:
                with ui.step('Countries'):
                    selectedRedCountries = ui.select(redTeamCountries, with_input=True, multiple=True,
                                                     label='Countries') \
                        .classes('w-64').props('use-chips').bind_value_to(selected_values, 'red_countries')
                    with ui.stepper_navigation():
                        ui.button('Next', on_click=stepper.next)
                with ui.step('Units'):


                    def update_team_units():
                        if unitInput.value and whereInput.value:
                            redTeamUnits.append({"unit": unitInput.value, "where": whereInput.value})
                            redTeamUnitsTable.rows = redTeamUnits
                            unitInput.value = ''
                            whereInput.value = ''

                    # def add_row() -> None:
                    #     new_id = max((dx['id'] for dx in redTeamUnitsTable.rows), default=-1) + 1
                    #     redTeamUnitsTable.rows.append({'id': new_id, 'unit': units[0], 'where': selectedRedCountries.value[0]})
                    #     # ui.notify(f'Added new row with ID {new_id}')
                    #     redTeamUnitsTable.update()
                    #
                    # def rename(e: events.GenericEventArguments) -> None:
                    #     for row in redTeamUnitsTable.rows:
                    #         if row['id'] == e.args['id']:
                    #             row.update(e.args)
                    #     # ui.notify(f'Updated rows to: {redTeamUnitsTable.rows}')
                    #     redTeamUnitsTable.update()
                    #
                    # def delete(e: events.GenericEventArguments) -> None:
                    #     redTeamUnitsTable.rows[:] = [row for row in redTeamUnitsTable.rows if row['id'] != e.args['id']]
                    #     # ui.notify(f'Deleted row with ID {e.args["id"]}')
                    #     redTeamUnitsTable.update()

                    with ui.row().style("width: 100%; gap: 10%"):
                        with ui.card().style("width: 45%;"):
                            unitInput = ui.select(units, label='Unit', with_input=True, multiple=False).style("width: 100%;")
                            whereInput = ui.select(redTeamCountries, label='Where', with_input=True,  multiple=False).style(
                                "width: 100%;")
                            ui.button("Add", on_click=update_team_units).style("margin-left: auto;")
                        columns = [
                            {'name': 'unit', 'label': 'Unit', 'field': 'unit', 'required': True, 'align': 'left'},
                            {'name': 'where', 'label': 'Where', 'field': 'where', 'required': True, 'align': 'left'},
                        ]

                        # columns = [
                        #     {'name': 'unit', 'label': 'Unit', 'field': 'unit', 'align': 'left'},
                        #     {'name': 'where', 'label': 'Where', 'field': 'where', 'align': 'left'},
                        # ]
                        # rows = [
                        #     {'id': 0, 'unit': 'Power plant', 'where': 'XX'},
                        #     {'id': 1, 'unit': 'Infrastructure', 'where': 'YY'}
                        # ]

                        redTeamUnitsTable = ui.table(columns=columns, rows=[], row_key="name").style(
                            "width: 45%; min-height: 212px;")
                    #                         redTeamUnitsTable.add_slot('header', r'''
                    #                             <q-tr :props="props">
                    #                                 <q-th auto-width />
                    #                                 <q-th v-for="col in props.cols" :key="col.name" :props="props">
                    #                                     {{ col.label }}
                    #                                 </q-th>
                    #                             </q-tr>
                    #                         ''')
                    #                         redTeamUnitsTable.add_slot('body', r'''
                    #                             <q-tr :props="props">
                    #                                 <q-td auto-width >
                    #                                     <q-btn size="sm" color="warning" round dense icon="delete"
                    #                                         @click="() => $parent.$emit('delete', props.row)"
                    #                                     />
                    #                                 </q-td>
                    #
                    #
                    #
                    #                                 <q-td key="unit" :props="props">
                    #                                     {{ props.row.unit }}
                    #                                     <q-popup-edit v-model="props.row.name" v-slot="scope"
                    #                                         @update:model-value="() => $parent.$emit('rename', props.row)"
                    #                                     >
                    #                                         <q-input v-model="scope.value" dense autofocus counter @keyup.enter="scope.set" />
                    #                                     </q-popup-edit>
                    #                                 </q-td>
                    #
                    #
                    #
                    #
                    #                                 <q-td key="where" :props="props">
                    #     <q-select
                    #         v-model="props.row.where"
                    #         :options="units"
                    #         emit-value
                    #         map-options
                    #         fill-input
                    #         dense
                    #         autofocus
                    #         @input="$parent.$emit('rename', props.row)"
                    #     />
                    # </q-td>
                    #                             </q-tr>
                    #                         ''')
                    #                         with redTeamUnitsTable.add_slot('bottom-row'):
                    #                             with redTeamUnitsTable.cell().props('colspan=3'):
                    #                                 ui.button('Add row', icon='add', color='accent', on_click=add_row).classes('w-full')
                    #                         redTeamUnitsTable.on('rename', rename)
                    #                         redTeamUnitsTable.on('delete', delete)
                    with ui.stepper_navigation():
                        ui.button('Next', on_click=stepper.next)
                        ui.button('Back', on_click=stepper.previous).props('flat')
                with ui.step('Finish'):
                    ui.label('Red team data is loaded')
                    with ui.stepper_navigation():
                        ui.button('Back', on_click=stepper.previous).props('flat')

        with ui.card().classes('').style(
                'width: 50%;  height: fit-content; min-height: 200px; align-items: center; margin-left: 20px;'):
            with ui.element('div').classes('mt-2 py-2 px-8 bg-blue-700 rounded-lg'):
                ui.label('Blue Team').classes('text-white')
            with ui.stepper().props('vertical').classes('w-full') as stepper:
                with ui.step('Countries'):
                    selectedBlueCountries = ui.select(blueTeamCountries, with_input=True, multiple=True,
                                                      label='Countries') \
                        .classes('w-64').props('use-chips').bind_value_to(selected_values, 'blue_countries')
                    with ui.stepper_navigation():
                        ui.button('Next', on_click=stepper.next)
                with ui.step('Units'):


                    def update_blue_team_units():
                        if blueUnitInput.value and blueWhereInput.value:
                            blueTeamUnits.append({"unit": blueUnitInput.value, "where": blueWhereInput.value})
                            blueTeamUnitsTable.rows = blueTeamUnits
                            blueUnitInput.value = ''
                            blueWhereInput.value = ''

                    with ui.row().style("width: 100%; gap: 10%"):
                        with ui.card().style("width: 45%;"):
                            blueUnitInput = ui.select(units, label='Unit', multiple=False).style("width: 100%;")
                            blueWhereInput = ui.select(blueTeamCountries, label='Where', multiple=False).style(
                                "width: 100%;")
                            ui.button("Add", on_click=update_blue_team_units).style("margin-left: auto;")
                        columns = [
                            {'name': 'unit', 'label': 'Unit', 'field': 'unit', 'required': True, 'align': 'left'},
                            {'name': 'where', 'label': 'Where', 'field': 'where', 'required': True,
                             'align': 'left'},
                        ]

                        blueTeamUnitsTable = ui.table(columns=columns, rows=[], row_key="name").style(
                            "width: 45%; min-height: 212px;")
                    with ui.stepper_navigation():
                        ui.button('Next', on_click=stepper.next)
                        ui.button('Back', on_click=stepper.previous).props('flat')
                with ui.step('Finish'):
                    ui.label('Blue team data is loaded')
                    with ui.stepper_navigation():
                        ui.button('Back', on_click=stepper.previous).props('flat')
