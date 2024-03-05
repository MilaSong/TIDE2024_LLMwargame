import json
from pprint import pprint

from resources.knowlage import ExternalDatabase
from agents.gpt import GPT

# system_prompt = """As a data analyst conducting research on Multi-Domain Operations (MDO), I am exploring the
# strategic and tactical units within various domains of military operations, including maritime, land, air, space,
# and cyberspace. My objective is to generate a comprehensive list of unit types.
#
# Request Format:
#
# Please provide a comprehensive list of possible military units in a specified domain for a given country.
#
# %s
#
# Response Structure:
#
# json
#
# [
#     {
#         "domain": "Specified Domain (e.g., land, maritime, air, space, cyberspace)",
#         "description": "A brief comment on the units in the specified domain for the country",
#         "range: "Provide the operational range of the action in kilometers (e.g., 5, 10, 50, 100 km) where applicable. For actions in domains where a physical range is not relevant (e.g., certain cyberspace operations), specify as "Not Applicable" instead of "0" to indicate the nature of the action does not involve a measurable physical distance.
#         "combat_strength": "Estimated combat strength of a single division size involved in the action in terms of personnel, equipment, or other relevant metrics",
#         "size" : "Estimated size of the single unit that could be involved in the action (e.g., number of personnel, number of vehicles, etc.)",
#         "can_be_offensive": "True/False",
#         "can_be_defensive": "True/False",
#         "can_be_destroyed": "True/False",
#         "can_be_repaired": "True/False",
#     }
#
#     ... // (4-9 more units)
# ]
#
# This structured approach will provide a clear and detailed view of military units within a specific domain,
# aiding in the comprehensive analysis of MDO capabilities and strategies."""

system_prompt = """
As a data analyst delving into Multi-Domain Operations (MDO) research, I am tasked with dissecting the intricate layers of strategic and tactical units spread across the diverse military domains: maritime, land, air, space, and cyberspace. The core of my investigation aims to meticulously catalog the myriad of unit types within each domain for a nuanced country-specific analysis.

Request Format:

In pursuit of this goal, I request a detailed enumeration of military units within a specified domain for a chosen country. The information should encapsulate not only the variety and scope of these units but also their operational parameters and potential roles in both offensive and defensive strategies.

%s

Response Structure:

The desired output is a structured JSON array, each object within embodying a specific military unit. The structure is as follows:

json

[
    {
        "domain": "The specified domain (e.g., land, maritime, air, space, cyberspace)",
        "description": "A concise overview of the unit's role and capabilities within the context of the specified domain for the selected country",
        "range": "Operational range in kilometers where applicable. For non-physical domains like cyberspace, use 'Not Applicable'",
        "combat_strength": "An estimation of the unit's combat efficacy, articulated through personnel numbers, equipment count, or other pertinent metrics",
        "size": "The typical composition of the unit in terms of personnel or equipment, aiming to provide a clear picture of a deployable unit size for balanced war gaming scenarios",
        "can_be_offensive": "Indicates if the unit has offensive capabilities (True/False)",
        "can_be_defensive": "Indicates if the unit can perform defensive operations (True/False)",
        "can_be_destroyed": "States the unit's vulnerability to being incapacitated or destroyed (True/False)",
        "can_be_repaired": "Specifies the unit's potential for repair or replenishment after sustaining damage (True/False)"
    }
    ... // Additional units (4-9 more)
]

"""


def generate_units(country, domain):
    print(f"Getting {country} {domain} domain actions")
    docs = ExternalDatabase.get(country, domain)
    print(f"Got {len(docs)} docs")
    modified_system_prompt = system_prompt
    if docs:
        raw_text = "\n\n".join(docs)
        modified_system_prompt = system_prompt % f"""This is additional information about {country} and {domain} domain:\n\n{raw_text}"""

    print("modified_system_prompt", modified_system_prompt)

    response = GPT.get_response(
        [
            {"role": "system", "content": modified_system_prompt},
            {"role": "system", "content": f"Provide a list of {domain} units for the {country} country"}
        ], max_tokens=2000
    )
    # "gpt-35-16k"
    return response


if __name__ == '__main__':
    domain = "land"
    country = "Russia"
    response = generate_units(country, domain)
    pprint(response)
    with open(f"{domain}_{country}.json", "w") as f:
        json.dump(response, f, indent=4, ensure_ascii=False)

# for domain in ["land", "maritime", "air", "space", "cyberspace"]:
#     for country in ["Russia", "Lithuania"]:
#         response = GPT.get_response(
#             [
#                 {"role": "system", "content": system_prompt},
#                 {"role": "system", "content": f"Provide a list of {domain} domain actions for the {country} country"}
#             ]
#         )
#         print(response)
#         with open(f"{domain}_{country}.json", "w") as f:
#             json.dump(response, f, indent=4, ensure_ascii=False)

# domain = "land"
# country = "Lithuania"
# response = GPT.get_response(
#             [
#                 {"role": "system", "content": system_prompt},
#                 {"role": "system", "content": f"Provide a list of {domain} domain actions for the {country} country"}
#             ]
#         )
# pprint(response)
