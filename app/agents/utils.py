import logging

from agents.gpt import GPT

logger = logging.getLogger(__name__)

def range_to_km(range):
    logger.debug(f"Converting range to km: {range}")
    response = GPT.get_response([
        {"role": "system", "content": "Convert range to km. If not applicable, return 0, return only number so it can be parsed to int. If it is a range return random number from the range"},
        {"role": "user", "content": range}
    ])
    logger.debug(f"Range to km response: {response}")
    try:
        logger.debug(f"Parsed range to km: {int(response)}")
        return int(response)
    except ValueError:
        return 0

if __name__ == '__main__':
    range = range_to_km("400-600 km")
    print(range)
    range = range_to_km("Not Applicable")
    print(range)