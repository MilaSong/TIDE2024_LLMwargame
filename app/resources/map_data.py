import traceback

import geopandas as gpd
from gadm import GADMDownloader

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class MapDatabaseDatabase:
    """
    Map Database to store information about countries.

    _data = {
        "Lithuania": {
            "center": {
                [ 54.6872, 25.2797]
            },
            "county": {
                "Kauno": {
                    "center": {
                        [ 54.6872, 25.2797]
                    },
                    "polygons": [
                        {
                            [ 54.6872, 25.2797],
                            [ 54.6872, 25.2797],
                            [ 54.6872, 25.2797]
                        }
                    ]
                }
            }
        }




    """
    _path = Path(__file__).parent.joinpath("./map_data.json")
    _data = {}
    _hashes = set()

    @classmethod
    def save(cls):
        cls._path.write_text(json.dumps(cls._data, indent=4, ensure_ascii=False))

    @classmethod
    def load(cls):
        if cls._path.exists():
            cls._data = json.loads(cls._path.read_text())
        else:
            cls.save()

    @classmethod
    def download(cls, country):
        def get_shape(country_name, ad_level=1, reduce=50):
            downloader = GADMDownloader(version="4.0")
            gdf = downloader.get_shape_data_by_country_name(country_name=country_name, ad_level=ad_level)
            assert isinstance(gdf, gpd.GeoDataFrame)
            # extract names of provinces
            result = []
            for county, polygon_list in zip(list(gdf["NAME_1"]), list(gdf["geometry"])):
                polygons = []
                # print(county)
                # print(list(poly.geoms))
                for polygon in list(polygon_list.geoms):
                    # POLYGON to list
                    # filter out smaller polygons
                    if len(polygon.exterior.coords) < 10:
                        continue
                    list_of_coords = list(polygon.exterior.coords)
                    # print(county, len(list_of_coords))
                    for i, (x, y) in enumerate(list_of_coords):
                        if i % reduce == 0:
                            polygons.append((y, x))
                result.append((county, polygons))
            return result

        try:
            result = get_shape(country)
            cls._data[country] = {
                "county": {}
            }
            for county, polygons in result:
                cls._data[country]["county"][county] = {
                    "center": [
                        sum([y for y, x in polygons]) / len(polygons),
                        sum([x for y, x in polygons]) / len(polygons)
                    ],
                    "polygons": polygons
                }
            cls.save()
        except Exception as e:
            logger.error(f"Failed to download country {country}.")
            logger.error(e)
            traceback.print_exc()
            return

    @classmethod
    def get(cls, country):
        if country not in cls._data:
            try:
                cls.download(country)
            except Exception as e:
                logger.error(f"Failed to download country {country}.")
                logger.error(e)
                traceback.print_exc()
                return []
        return cls._data[country]

    @staticmethod
    def find_polygon_centroid(points):
        """
        Calculate the centroid of a polygon given by points.

        Args:
        points (list of tuples): List of (x, y) tuples representing the vertices of the polygon.

        Returns:
        (float, float): The (x, y) coordinates of the centroid.
        """
        x_coords = [p[0] for p in points]
        y_coords = [p[1] for p in points]
        centroid_x = sum(x_coords) / len(points)
        centroid_y = sum(y_coords) / len(points)
        return centroid_x, centroid_y

    @classmethod
    def get_all(cls):
        return cls._data


MapDatabaseDatabase.load()

if __name__ == '__main__':
    MapDatabaseDatabase.download("Lithuania")
