from nicegui import ui

from resources.map_data import MapDatabaseDatabase
from resources.map_utils import get_neighboring_pairs

map_data = {
    "Lithuania": {
        **MapDatabaseDatabase.get('Lithuania'),
        "color": "blue",
    },
    "Latvia": {
        **MapDatabaseDatabase.get('Latvia'),
        "color": "blue",
    },
    "Estonia": {
        **MapDatabaseDatabase.get('Estonia'),
        "color": "blue",
    },
    "Belarus": {
        **MapDatabaseDatabase.get('Belarus'),
        "color": "red",
    },
    # "Russia": {
    #     "color": "red",
    #     "description": "Russia",
    #     "polygons": get_shape('Russia')
    # },
}

# def handle_draw(e: events.GenericEventArguments):
#     if e.args['layerType'] == 'marker':
#         map.marker(latlng=(e.args['layer']['_latlng']['lat'],
#                            e.args['layer']['_latlng']['lng']))
#     if e.args['layerType'] == 'polyline':
#         map.generic_layer(name='polyline', args=[e.args['layer']['_latlngs']])
#     if e.args['layerType'] == 'polygon':
#         map.generic_layer(name='polygon', args=[e.args['layer']['_latlngs']])


# def handle_click(e: events.GenericEventArguments):
#     print(e.args)
#
#
# def handle_right_click(e: events.GenericEventArguments):
#     pprint(e.args)
#     # delete marker
#     if e.args['which'] == 3:
#         # get type of layer
#         layer_type = e.args['layer']['_layers']
#         print(layer_type)

# infrastucture = [
#     {'name': 'Vilnius', 'location': (54.6872, 25.2797), "description": "Capital of Lithuania"},
#     {'name': 'Kaunas', 'location': (54.8969, 23.8864), "description": "Second largest city in Lithuania"},
#     {'name': 'Klaipėda', 'location': (55.7033, 21.1443), "description": "Third city in Lithuania"},
# ]

# draw_control = {
#     'draw': {
#         'polygon': True,
#         'marker': True,
#         'circle': True,
#         'rectangle': True,
#         'polyline': True,
#         'circlemarker': True,
#     },
#     'edit': False,
#     'remove': True,
# }
# make height 100%
map = ui.leaflet(center=(55.505, 23.09), zoom=6, options={
    "dragging": False,
    "touchZoom": False,
    "zoomControl": False,
    "scrollWheelZoom": False,
    "tap": False,
    "doubleClickZoom": False,
}).style("height: 800px")
map.bounds = [[55.505, 23.09], [56.505, 24.09]]
# make map static
map.dragging = False
map.touch_zoom = False
map.double_click_zoom = False
map.scroll_wheel_zoom = False
map.box_zoom = False

neighboring_pairs = get_neighboring_pairs(["Lithuania", "Latvia"], ["Belarus"])
for neighboring_pair in neighboring_pairs:
    region_1, region_2 = neighboring_pair['pair']
    region_1_center = region_1['center']
    region_2_center = region_2['center']
    print(f"Region 1 center: {region_1_center}")
    print(f"Region 2 center: {region_2_center}")
    map.generic_layer(name='polyline', args=[[region_1_center, region_2_center], {'color': 'black', 'weight': 5}])
    # map.generic_layer(name='polyline', args=[[region_1_center, region_2_center], {'color': 'red', 'weight': 5}])

# for pair in neighboring_pairs draw a polyline
# for pos1, pos2 in neighboring_pairs:
#     print(f"Pos1: {pos1}")
#     print(f"Pos2: {pos2}")
# pos1_center = pos1['center']
# pos2_center = pos2['center']


# map.on("mousedown", lambda e: print(e.args))
# map.on("mouseup", lambda e: print(e.args))

# map.on('draw:created', handle_draw)
# map.on('click', handle_click)
# map.on('contextmenu', handle_right_click)
# map.on("mouseover", lambda e: print(e.args))
# map.on("layeradd", lambda e: print(e.args))

# draw line between two points
# map.generic_layer(name='line', args=[[(54.6872, 25.2797), (54.8969, 23.8864)], {'color': 'red', 'width': 5}])

# draw polyline
# line = map.generic_layer(name='polyline',
#                          args=[[(54.6872, 25.2797), (54.8969, 23.8864), (55.7033, 21.1443)], {'color': 'green'}])

for country, data in map_data.items():
    print(f"Country: {country}")
    print(f"Data: {data}")
    for name, county_data in data["county"].items():
        center = county_data['center']
        print(f"Name: {name}")
        print(f"Center: {center}")
        map.marker(latlng=center)
        map.generic_layer(name='polygon', args=[county_data["polygons"], {'color': data['color']}])

        # for polygon in county_data['polygons']:
        #     print(f"Polygon: {polygon}")
        # convert from list to tuple
        # for i, point in enumerate(polygon):
        #     print(f"Point: {point}")
        # polygon = [tuple(point[0],point[1]) for point in polygon]
        # map.generic_layer(name='polygon', args=[polygon, {'color': data['color']}])
        #     map.marker(latlng=center)
    # map.generic_layer(name='polygon', args=[polygon, {'color': data['color']}])
# draw polygone
# map.generic_layer(name='polygon',
#                   args=[[(54.6872, 25.2797), (54.8969, 23.8864), (55.7033, 21.1443)], {'color': 'blue'}])
# draw polygon
# map.generic_layer(name='polygon', args=[[(54.6872, 25.2797), (54.8969, 23.8864), (55.7033, 21.1443)], {'color': 'blue'}])


# for place in infrastucture:
#     marker = map.marker(latlng=place['location'])
#     marker.draggable(True)

#     print(marker.__dir__())

# ui.label().bind_text_from(map, 'center', lambda center: f'Center: {center[0]:.3f}, {center[1]:.3f}')
# ui.label().bind_text_from(map, 'zoom', lambda zoom: f'Zoom: {zoom}')


# with ui.grid(columns=2):
#     ui.button('London', on_click=lambda: map.set_center((51.505, -0.090)))
#     ui.button('Berlin', on_click=lambda: map.set_center((52.520, 13.405)))
#     ui.button(icon='zoom_in', on_click=lambda: map.set_zoom(map.zoom + 1))
#     ui.button(icon='zoom_out', on_click=lambda: map.set_zoom(map.zoom - 1))

ui.run()
