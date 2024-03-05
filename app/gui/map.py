from nicegui import ui

from resources.map_data import MapDatabaseDatabase
from resources.map_utils import get_neighboring_pairs


def create_map():
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
            "color": "red"
        }
    }

    map = ui.leaflet(center=(55.505, 23.09), zoom=6, options={
        "dragging": False,
        "touchZoom": False,
        "zoomControl": False,
        "scrollWheelZoom": False,
        "tap": False,
        "doubleClickZoom": False,
    }).style("height: 500px")

    map.tile_layer(
        url_template='https://tiles.stadiamaps.com/tiles/stamen_toner_background/{z}/{x}/{y}{r}.png',
        options={
            'maxZoom': 17,
            'attribution':
                'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | '
                'Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
        },
    )

    map.bounds = [[55.505, 23.09], [56.505, 24.09]]

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
        map.generic_layer(name='polyline', args=[[region_1_center, region_2_center], {'color': 'black', 'weight': 5}])

    for country, data in map_data.items():
        # print(f"Country: {country}")
        # print(f"Data: {data}")
        for name, county_data in data["county"].items():
            center = county_data['center']
            # print(f"Name: {name}")
            # print(f"Center: {center}")
            map.marker(latlng=center)
            map.generic_layer(name='polygon', args=[county_data["polygons"], {'color': data['color']}])


# ui.run()
