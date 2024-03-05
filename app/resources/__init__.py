import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

"""
This module contains the gameplay state and the resources of types and units
"""


def load_from_json(path):
    """
    Load a json file
    :param path:
    :return:
    """
    logger.info(f"Loading {path} from json")
    file = Path(__file__).parent / path
    return json.loads(file.read_text())


class Dictionary:
    """
    This class contains the resources of types and units
    """

    types = load_from_json("types.json")
    units = load_from_json("units.json")
    domains = ["land", "maritime", "air", "space", "cyberspace"]

    @classmethod
    def get_unit_description(cls, unit_name):
        """
        Get the description of a unit
        :param unit_name:
        :return:
        """
        for unit in cls.units:
            if unit["name"] == unit_name:
                return unit["description"]
        return None

    @classmethod
    def get_unit_domain(cls, unit_name):
        """
        Get the domain of a unit
        :param unit_name:
        :return:
        """
        for unit in cls.units:
            if unit["name"] == unit_name:
                return unit["domain"]
        return None

    @classmethod
    def get_domains(cls):
        """
        Get the domains
        :return:
        """
        return cls.domains


    @classmethod
    def get_json_types(cls):
        return cls.types

    @classmethod
    def get_json_units(cls):
        return cls.units

if __name__ == '__main__':
    print(Dictionary.get_unit_description("army base"))
    print(Dictionary.get_unit_domain("army base"))
    print(Dictionary.get_domains())

