import asyncio
import copy
import json
import logging
import traceback
import hashlib
from pathlib import Path

from agents.about_file import analyze_text

logger = logging.getLogger(__name__)


def get_hash(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()


class ExternalFileDatabase:
    _path = Path(__file__).parent.joinpath("./file_external.json")
    _data = {}

    @classmethod
    def save(cls):
        cls._path.write_text(json.dumps(cls._data, indent=4, ensure_ascii=False))

    @classmethod
    def load(cls):
        if cls._path.exists():
            cls._data = json.loads(cls._path.read_text())
        # cls._data = {}
        else:
            cls.save()

    @classmethod
    async def add(cls, text):
        text_hash = get_hash(text)
        if text_hash in cls._data:
            raise ValueError("Text already exists")
        try:
            json_response = await analyze_text(text)
            json_response['hash'] = text_hash
            cls._data[text_hash] = json_response
            cls.save()
        except Exception as e:
            traceback.print_exc()
            raise ValueError(f"Failed to analyze text: {e}")

    @classmethod
    def get_all(cls):
        return list(cls._data.values())

    @classmethod
    def delete(cls, hash_code):
        if hash_code in cls._data:
            del cls._data[hash_code]
            cls.save()
        else:
            raise ValueError("Text not found")


ExternalFileDatabase.load()

if __name__ == '__main__':
    military_text = """The Lithuanian Armed Forces (Lithuanian: Lietuvos ginkluotosios pajėgos) are the military of Lithuania. The Lithuanian Armed Forces consist of the Lithuanian Land Forces, the Lithuanian Naval Force, the Lithuanian Air Force and the Lithuanian Special Operations Force. In wartime, the Lithuanian State Border Guard Service (which is under the supervision of the Ministry of the Interior in peacetime) becomes part of the Lithuanian Armed Forces. A special security department handles VIP protection and communications security.
The purpose of the Lithuanian Armed Forces are to be the principal deterrent against any security threat to the nation. Lithuania's defence system is based on the concept of "total and unconditional defence" mandated by Lithuania's National Security Strategy. The goal of Lithuania's defence policy is to prepare their society for general defence and to integrate Lithuania into Western security and defence structures. The Ministry of National Defence is responsible for combat forces, search and rescue, and intelligence operations.[4]
Male conscription is in place since 2015, when it was reinstated after being ended in 2008, due to concerns about the geopolitical environment in light of the Russo-Ukrainian War.[5]
In early 2022, Lithuania's defence budget for 2022 was approximately €1.05 billion,[1][c] but it was increased to €1.5 billion on 17 March 2022.[6] """

    asyncio.run(ExternalFileDatabase.add(military_text))
