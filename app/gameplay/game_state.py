import json
import logging
from pathlib import Path

from resources import Dictionary


class GameState:
    state = None
    file_path = Path(__file__).parent.joinpath("./game_state.json")
    logger = logging.getLogger(__name__)

    @classmethod
    def get_team(cls, team_name):
        cls.logger.debug(f"Getting team {team_name}")
        return [team for team in cls.state["teams"] if team["name"] == team_name][0]

    @classmethod
    def append_team(cls, team_name):
        cls.state["teams"].append(team_name)

    @classmethod
    def get_units(cls, team_name):
        cls.logger.debug(f"Getting units for {team_name}")
        return cls.state["units"][team_name]

    @classmethod
    def get_events(cls):
        cls.logger.debug(f"Getting events")
        return cls.state["events"]

    @classmethod
    def get_wining_by_domain(cls, domain):
        cls.logger.debug(f"Getting winning for {domain}")
        return 33, 33
        # red = cls.state["winning"]["red"][domain]
        # blue = cls.state["winning"]["blue"][domain]
        # return blue / (red + blue) * 100, red

    @classmethod
    def update_winning(cls, domain, team_name, value):
        cls.logger.debug(f"Updating winning for {team_name} in {domain} by {value}")
        cls.state["winning"][team_name][domain] += value
        cls.logger.info(f"Updated winning for {team_name} in {domain} by {value}")

    @classmethod
    def add_event(cls, event):
        cls.logger.debug(f"Adding event {event}")
        cls.state["events"].append(event)
        cls.logger.info(f"Added event {event}")

    @classmethod
    def get_next(cls):
        cls.logger.debug(f"Getting next team")
        return cls.state["next"]

    @classmethod
    def get_opponent(cls, team_name):
        cls.logger.debug(f"Getting opponent for {team_name}")
        if team_name == "red":
            return "blue"
        else:
            return "red"

    @classmethod
    def set_next(cls, team_name):
        cls.logger.info(f"Setting next team to {team_name}")
        cls.state["next"] = team_name

    @classmethod
    def get_team_state(cls, team):
        cls.logger.debug(f"Getting state for {team}")
        return cls.state[team]

    @classmethod
    def get_team_units(cls, team):
        cls.logger.debug(f"Getting units for {team}")
        return cls.state["units"][team]

    @classmethod
    def append_team_units(cls, unit, team):
        cls.state["units"][team].append(unit)

    @classmethod
    def get_team_units_str(cls, team):
        cls.logger.debug(f"Getting units for {team}")
        results = []
        for unit in cls.state["units"][team]:

            domain = Dictionary.get_unit_domain(unit['name'])
            if unit["location"]:
                results.append(f"{domain}_{unit['name']}_{unit['condition']}_{unit['location']}")
            else:
                results.append(f"{domain}_{unit['name']}_{unit['condition']}")
        return results

    @classmethod
    def init(cls):
        cls.logger.info("Initializing gameplay state")
        if cls.state is None:
            cls.load("demo_state.json")

    @classmethod
    def reset(cls):
        cls.logger.info("Resetting gameplay state")
        cls.load("demo_state.json")

    @classmethod
    def save(cls):
        cls.logger.debug("Saving gameplay state")
        cls.file_path.write_text(json.dumps(cls.state, indent=4, ensure_ascii=False))

    @classmethod
    def load(cls, path="game_state.json"):
        cls.logger.debug(f"Loading gameplay state from {path}")
        cls.state = json.loads(Path(__file__).parent.joinpath(path).read_text())

    @classmethod
    def get_state(cls):
        return cls.state


GameState.init()
