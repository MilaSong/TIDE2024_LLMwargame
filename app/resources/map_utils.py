import math

from resources.map_data import MapDatabaseDatabase


def get_neighboring_pairs(blue_teams, red_teams):
    blue_teams = ["Lithuania", "Latvia"]
    red_teams = ["Belarus"]

    data = [
        #     {
        #         "country": "Lithuania",
        #         "county": "Alytus",
        #         "center": [54.40, 24.05]
        #         "team": "blue
        #     },
    ]

    for country in blue_teams:
        for county in MapDatabaseDatabase.get(country)["county"]:
            data.append({
                "country": country,
                "county": county,
                "center": MapDatabaseDatabase.get(country)["county"][county]["center"],
                "team": "blue"
            })

    for country in red_teams:
        for county in MapDatabaseDatabase.get(country)["county"]:
            data.append({
                "country": country,
                "county": county,
                "center": MapDatabaseDatabase.get(country)["county"][county]["center"],
                "team": "red"
            })

    # pprint(data)

    def haversine(lon1, lat1, lon2, lat2):
        # Convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))
        r = 6371  # Radius of Earth in kilometers
        return c * r

    # Set the search radius in kilometers
    search_radius = 230  # Adjust this value as needed

    # Find neighbouring data
    neighbouring_pairs = []

    for province_a in data:
        if province_a['team'] == 'blue':
            for province_b in data:
                if province_b['team'] == 'red':
                    distance = haversine(province_a['center'][1], province_a['center'][0], province_b['center'][1],
                                         province_b['center'][0])
                    if distance <= search_radius:
                        neighbouring_pairs.append({
                            "pair": [province_a, province_b],
                            "distance": distance
                        })

    return neighbouring_pairs


if __name__ == '__main__':
    pairs = get_neighboring_pairs(["Lithuania", "Latvia"], ["Belarus"])
    for pair in pairs:
        print(pair)
