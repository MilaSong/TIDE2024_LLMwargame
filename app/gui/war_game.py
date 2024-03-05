import json
import logging
import random

from nicegui import ui, events

import plotly.graph_objs as go

from gameplay.game_state import GameState
from gui.components import create_bar_chart, create_table_of_units, create_timeline
from gui.map import create_map
from gui.modal.select_form import show_new_move_dialog

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# ui.add_head_html('''
# <style>
# .zoom {
#   padding: 10px;
#   background-color: green;
#   transition: transform .3s;
#   margin: 0 auto;
#   z-index: 1;
# }
#
# .zoom:hover {
#   transform: scale(1.1); /* (150% zoom - Note: if the zoom is too large, it will go outside of the viewport) */
#   z-index: 2;
# }
#
# .text-subtitle {
#   font-size: .675rem;
#   font-weight: 500;
#   line-height: 1.375rem;
#   letter-spacing: .00714em;
#   color: grey;
# }
# </style>
# ''')


def read_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data


def save_to_file(file_path):
    data = {}
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def show_gauge_chart(domain):
    ratio = GameState.get_wining_by_domain(domain)
    data = [
        go.Indicator(
            mode='gauge',
            value=ratio[0],
            title={'text': domain},
            gauge={
                'axis': {'range': [None, 100], 'visible': False},
                'bar': {'color': '#DC2626', 'thickness': 1},
                'steps': [{'range': [0, 100], 'color': '#1D4ED8'}],
                'threshold': {
                    'thickness': 1, 'value': ratio[1]}
            }
        )
    ]
    layout = go.Layout(
        title={'text': '', 'y': 0.8, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
        font=dict(color='black', family="sans-serif", size=12),
        paper_bgcolor='rgba(255, 255, 255, 0)',
        plot_bgcolor='rgba(255, 255, 255, 0)',
        margin=dict(l=0, r=0, t=0, b=0),
        width=230,
        height=200
    )
    fig = go.Figure(data=data, layout=layout)
    ui.plotly(fig)


def send_message() -> None:
    print("Veikia")


def dashboard():
    with ui.header().classes(replace='row items-center') as header:
        ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')

    with ui.left_drawer().classes('bg-blue-100').props('width=170') as left_drawer:
        ui.button('New', on_click=lambda: ui.open("/new_game"), icon='settings').props('flat color=blue')
        ui.button('Wargame', on_click=lambda: ui.open("/"), icon='sports').props(
            'flat color=blue').classes(
            'justify-between')
        ui.button('Config', on_click=lambda: ui.open("/config"), icon='settings').props('flat color=blue')
        ui.button('Vault', on_click=lambda: ui.open("/vault"), icon='pool').props('flat color=blue')


# @ui.refreshable
def create_charts():
    with ui.row().style("display: flex; flex-wrap: nowrap; width: 100%; margin-left: auto; margin-right: auto;"):
        # ui.label("Red team moves").style("font-weight: bold;").style("background-color: red; color: white;")
        ui.button("Make a move", on_click=lambda _: show_new_move_dialog())
        create_bar_chart("land")
        create_bar_chart("air")
        create_bar_chart("cyber")
        create_bar_chart("maritime")
        create_bar_chart("space")
        #

    # show_gauge_chart("land")
    # show_gauge_chart("air")
    # show_gauge_chart("cyber")
    # show_gauge_chart("maritime")
    # show_gauge_chart("space")

#
# def debug():
#     with ui.row().style("margin-left: auto; margin-right: auto;"):
#         def increase_red_land():
#             # print("Increase red land")
#             GameState.update_winning("land", "red", 10)
#             # print(GameState.get_wining_by_domain("land"))
#             # charts["land"].update()
#             create_charts.refresh()
#
#         ui.button("Increase Red Land", on_click=increase_red_land)
#
#         def add_event():
#             event = {
#                 "id": random.randint(0, 100),
#                 "title": "Started sanctions of Rus***",
#                 "description": "The blue team started sanctions",
#                 "team": "blue",
#                 "attacker": {
#                     "domain": "cyber",
#                     "unit": "ministry of economics",
#                     "location": None
#                 },
#                 "target": {
#                     "domain": "cyber",
#                     "unit": "banking system",
#                     "location": None
#                 },
#                 "outcomes": [
#                     {
#                         "domain": "cyber",
#                         "outcome": "Outcome of domain"
#                     }
#                 ]
#             }
#             GameState.add_event(event)
#             # timeline.refresh()
#
#         # def generate_actions()
#
#         ui.button("Add event", on_click=add_event)
#
#         def generate_actions():
#             cards.refresh()
#
#         ui.button("Generate actions", on_click=generate_actions)
#

# def team_move():
#     moving_team = GameState.get_next()
#     opponent_team = GameState.get_opponent(moving_team)
#     with ui.card().style("height: 200px; flex: 1;").classes("bg-slate-100"):
#         ui.label(f"Move {moving_team}").style("font-weight: bold;").style(
#             f'background-color: {moving_team}; color: white;')
#         ui.select(options=GameState.get_team_units_str(moving_team), new_value_mode='add', label='Select unit')
#         ui.select(options=GameState.get_team_units_str(opponent_team), new_value_mode='add', label='Select target unit')
#         ui.button("Get actions", on_click=lambda: execute_action(0)).style("margin-top: 10px;")


def create_unit_lists():
    with ui.row().style("display: flex; flex-wrap: nowrap; width: 100%; margin-left: auto; margin-right: auto;"):
        with ui.column().style("align-items: center; width: 50%;"):
            create_table_of_units("red")

        with ui.column().style("align-items: center; width: 50%;"):
            create_table_of_units("blue")


@ui.page('/')
def war_game():
    # ui.add_head_html('''
    #             <style>
    #                 .nicegui-content {
    #                     padding: 0;
    #                 }
    #                 .leaflet-bottom{
    #                     visibility: hidden;
    #                 }
    #             </style>
    #         ''')
    # debug()
    dashboard()
    ui.separator()
    with ui.column().classes("w-full").style("padding-left: 20px; padding-right: 20px; margin-top: 10px"):
        # ui.label("Winning conditions").style("margin-left: auto; margin-right: auto; font-weight: bold;")
        # with ui.row().style("margin-left: auto; margin-right: auto;"):
        create_charts()
        ui.separator()
        # ui.label("").style("margin-left: auto; margin-right: auto; font-weight: bold;")
        create_unit_lists()
        ui.separator()

        with ui.row().classes("flex-nowrap").style("width: 100%; margin-left: auto; margin-right: auto;"):
            # with ui.column().style("align-items: center; width: 20%;"):
            #     team_move()

            with ui.column().style("align-items: center; width: 60%;"):
                ui.label("Map").style("font-weight: bold;")
                draw_control = {
                    'draw': {
                        'polygon': True,
                        'marker': True,
                        'circle': True,
                        'rectangle': True,
                        'polyline': True,
                        'circlemarker': True,
                    },
                    'edit': False,
                }
                create_map()

                # def handle_draw(e: events.GenericEventArguments):
                #     print(e)
                #     if e.args['layerType'] == 'marker':
                #         m.marker(latlng=(e.args['layer']['_latlng']['lat'],
                #                          e.args['layer']['_latlng']['lng']))
                #     if e.args['layerType'] == 'polygon':
                #         m.generic_layer(name='polygon', args=[e.args['layer']['_latlngs']])

                # m = ui.leaflet(center=(56.88, 24.60), zoom=5, draw_control=draw_control).style("height: 500px;")
                # m.on('draw:created', handle_draw)
                # m.clear_layers()
                # m.tile_layer(
                #     url_template='https://tiles.stadiamaps.com/tiles/stamen_toner_background/{z}/{x}/{y}{r}.png',
                #     options={
                #         'maxZoom': 17,
                #         'attribution':
                #             'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | '
                #             'Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
                #     },
                # )
            # with ui.column().style("align-items: center;"):
            with ui.scroll_area().style("height: 600px;  width: 50%;"):
                create_timeline()
        # with ui.row().classes("flex-nowrap").style("gap: 20px; width: 100%; margin-left: auto; margin-right: auto;"):
        #     cards()


if __name__ == '__main__':
    ui.run()
