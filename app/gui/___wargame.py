# from nicegui import ui, events
# import plotly.graph_objs as go
#
#
# def show_gauge_chart(get_hum, title):
#     data = [
#         go.Indicator(
#             mode='gauge',
#             value=get_hum,
#             title={'text': title},
#             gauge={
#                 'axis': {'range': [None, 100], 'visible': False},
#                 'bar': {'color': '#DC2626', 'thickness': 1},
#                 'steps': [{'range': [0, 100], 'color': '#1D4ED8'}],
#                 'threshold': {
#                               'thickness': 1, 'value': get_hum}
#             }
#         )
#     ]
#     layout = go.Layout(
#         title={'text': '', 'y': 0.8, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
#         font=dict(color='black', family="sans-serif", size=12),
#         paper_bgcolor='rgba(255, 255, 255, 0)',
#         plot_bgcolor='rgba(255, 255, 255, 0)',
#         margin=dict(l=0, r=0, t=0, b=0),
#         width=230,
#         height=200
#     )
#     fig = go.Figure(data=data, layout=layout)
#     ui.plotly(fig)
#
#
# def show_bar_chart(red_value):
#     # import plotly.express as px
#     #
#     # custom_data = {
#     #     'year': [2002, 2002],
#     #     'pop': [16, 14],
#     #     'lifeExp': [60, 65],
#     #     'gdpPercap': [10000, 15000],
#     #     'country': ['A', 'B']
#     # }
#     #
#     # # Create a Plotly Express bar chart
#     # fig = px.bar(custom_data, x='year', y='pop',
#     #              hover_data=['lifeExp', 'gdpPercap'], color='country',
#     #              labels={'pop': '', 'year': ''},
#     #              # orientation='h',
#     #              height=200,
#     #              width=200)
#     # fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', showlegend=False, dragmode=False,
#     #     hovermode=False, margin=dict(l=0, r=0, t=0, b=0))
#     # fig.update_xaxes(visible=False)
#     # fig.update_yaxes(visible=False)
#     # ui.plotly(fig)
#     with ui.column().style("width: 100px"):
#         ui.label("Air").style("")
#         with ui.element('div').style("width: 100px; height: 50px; display: flex;"):
#             ui.element('div').style(f"background-color: red; width: {red_value}%;")
#             ui.element('div').style(f"background-color: blue; width: {100-red_value}%;")
#
#
# def send_message() -> None:
#     print("Veikia")
#
#
# def wargame():
#     ui.add_head_html('''
#                 <style>
#                     .nicegui-content {
#                         padding: 0;
#                     }
#                     .leaflet-bottom{
#                         visibility: hidden;
#                     }
#                 </style>
#             ''')
#     with ui.column().classes("w-full").style("padding-left: 20px; padding-right: 20px; margin-top: 10px"):
#         ui.label("Resources").style("margin-left: auto; margin-right: auto; font-weight: bold;")
#         with ui.row().style("margin-left: auto; margin-right: auto;"):
#             show_gauge_chart(50, "Space")
#             show_gauge_chart(50, "Air")
#             show_gauge_chart(50, "Ground")
#             show_gauge_chart(50, "Cyber")
#             show_gauge_chart(50, "Navy")
#         with ui.row().classes("flex-nowrap").style("width: 100%; margin-left: auto; margin-right: auto;"):
#             with ui.column().style("align-items: center; width: 50%;"):
#                 ui.label("Map").style("font-weight: bold;")
#                 draw_control = {
#                     'draw': {
#                         'polygon': True,
#                         'marker': True,
#                         'circle': True,
#                         'rectangle': True,
#                         'polyline': True,
#                         'circlemarker': True,
#                     },
#                     'edit': False,
#                 }
#
#                 def handle_draw(e: events.GenericEventArguments):
#                     print(e)
#                     if e.args['layerType'] == 'marker':
#                         m.marker(latlng=(e.args['layer']['_latlng']['lat'],
#                                          e.args['layer']['_latlng']['lng']))
#                     if e.args['layerType'] == 'polygon':
#                         m.generic_layer(name='polygon', args=[e.args['layer']['_latlngs']])
#                 m = ui.leaflet(center=(56.88, 24.60), zoom=5, draw_control=draw_control).style("height: 500px;")
#                 m.on('draw:created', handle_draw)
#                 m.clear_layers()
#                 m.tile_layer(
#                     url_template='https://tiles.stadiamaps.com/tiles/stamen_toner_background/{z}/{x}/{y}{r}.png',
#                     options={
#                         'maxZoom': 17,
#                         'attribution':
#                             'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | '
#                             'Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
#                     },
#                 )
#             with ui.column().style("align-items: center;"):
#                 ui.label("Timeline").style("font-weight: bold;")
#                 with ui.timeline(side='right').style("min-width: 50%;"):
#                     ui.timeline_entry('Large parts are rewritten to remove JustPy '
#                                           'and to upgrade to Vue 3 and Quasar 2.',
#                                           title='Release of 1.0',
#                                           subtitle='December 15, 2022',
#                                           icon='rocket')
#                     ui.timeline_entry('The first PyPI package is released.',
#                                           title='Release of 0.1',
#                                           subtitle='May 14, 2021',
#                                           color='blue')
#                     ui.timeline_entry('Rodja and Falko start working on NiceGUI.',
#                                           title='Initial commit',
#                                           subtitle='May 07, 2021',
#                                           color='red'
#                                           )
#
#         with ui.row().classes("flex-nowrap").style("gap: 20px; width: 100%; margin-left: auto; margin-right: auto;"):
#             with ui.card().classes("bg-slate-100").style("height: 200px; align-items: center; flex: 1;"):
#                 ui.label("Title").style("font-weight: bold;")
#                 ui.label("Subtitle")
#             ui.card().classes("bg-slate-100").style("height: 200px; flex: 1;")
#             ui.card().classes("bg-slate-100").style("height: 200px; flex: 1;")
#             ui.card().classes("bg-slate-100").style("height: 200px; flex: 1;")
#             ui.card().classes("bg-slate-100").style("height: 200px; flex: 1;")
#             with ui.card().classes("bg-neutral-400").style("height: 200px; flex: 2; align-items: center;"):
#                 ui.label("User input").style("font-weight: bold;")
#                 ui.input(placeholder='message').on('keydown.enter', send_message) \
#                         .props('rounded outlined input-class=mx-3').classes('flex-grow')
#
#     # with ui.row().style(""):
#     # show_bar_chart(50)
#
#         # show_bar_chart(50)
#
