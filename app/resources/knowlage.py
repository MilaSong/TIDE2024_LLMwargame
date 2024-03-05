import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class ExternalDatabase:
    """
    A simple external database to store information about countries.

    Data structure:

    data = {
     "lt" : {
      "land: ["Some text about lithuanian land forces"],
      "navy: ["Some text about lithuanian navy"],
    }
    """
    _path = Path(__file__).parent.joinpath("./external.json")
    _data = {}
    _hashes = set()

    @classmethod
    def save(cls):
        cls._path.write_text(json.dumps(cls._data, indent=4, ensure_ascii=False))
        # with open(__file__ / cls._path, "w") as file:
        #     logger.debug(f"Saving to {cls._path}")
        #     json.dump(cls._data, file, indent=4, ensure_ascii=False)

    @classmethod
    def load(cls):
        if cls._path.exists():
            cls._data = json.loads(cls._path.read_text())
            cls._calculate_hashes()
        else:
            cls.save()

    @classmethod
    def add(cls, country, domain, text):
        text_hash = hash(text)
        if text_hash in cls._hashes:
            raise ValueError("Text already exists")
        if country not in cls._data:
            cls._data[country] = {}
        if domain not in cls._data[country]:
            cls._data[country][domain] = []
        cls._data[country][domain].append(text)
        cls.save()

    @classmethod
    def get(cls, country, domain):
        if country not in cls._data:
            return []
        if domain not in cls._data[country]:
            return []
        return cls._data[country][domain]

    @classmethod
    def _calculate_hashes(cls):
        cls._hashes = set()
        for country, domains in cls._data.items():
            for domain, texts in domains.items():
                for text in texts:
                    cls._hashes.add(hash(text))


ExternalDatabase.load()

if __name__ == '__main__':
    ExternalDatabase.load()
    ExternalDatabase.add("lt", "land", "Some text about lithuanian land forces")
    ExternalDatabase.add("lt", "navy", "Some text about lithuanian navy")
