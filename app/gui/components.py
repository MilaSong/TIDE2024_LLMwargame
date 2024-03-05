from nicegui import ui

from gameplay.game_state import GameState


def create_bar_chart(domain):
    with ui.column().style("flex: 1;"):
        ui.label(domain).style("font-weight: bold; margin: auto;").style("text-align: center;")
        ui.linear_progress(value=0.4, color="red", show_value=False).style('height: 20px; margin: 10px;').style(
            f'background-color: blue;')


def create_table_of_units(team):
    background_color = "#ff00003d" if team == "red" else "#0000ff3d"
    # ui.label(f"{team} team Units").style("font-weight: bold;")

    columns = [
        {'name': 'name', 'label': 'Name', 'field': 'name', 'sortable': True, 'searchable': True,
         'align': 'left'},
        {'name': 'location', 'label': 'Location', 'field': 'location', 'sortable': True, 'searchable': True,
         'align': 'center'},
        {'name': 'condition', 'label': 'Condition', 'field': 'condition', 'sortable': True, 'searchable': True,
         'align': 'right'},
    ]

    units = GameState.get_team_units(team)
    with ui.expansion(f"{team.title()} team Units", icon='unit').classes('w-full').style(
            f"background-color: {background_color};"):
        with ui.scroll_area().style("height: 200px;"):
            ui.table(columns=columns, rows=units, row_key='name').style("width: 100%; flex: 1;")


@ui.refreshable
def create_timeline():
    events = GameState.get_events()
    ui.label("Timeline").style("font-weight: bold;")
    with ui.timeline(side='right').style(""):  # min-width: 50%;
        for event in events:
            ui.timeline_entry(event['description'],
                              title=event['title'],
                              subtitle=event['team'],
                              icon='rocket',
                              color='red' if event['team'] == 'red' else 'blue', )
