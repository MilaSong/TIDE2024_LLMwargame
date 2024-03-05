# import json
# from pprint import pprint
#
# from app.resources.knowlage import ExternalDatabase
# from app.agents.gpt import GPT
#
# system_prompt = """
# As a data analyst conducting research on Multi-Domain Operations (MDO), I am exploring the strategic and tactical actions within various domains of military operations, including maritime, land, air, space, and cyberspace. My objective is to analyze the potential offensive and defensive capabilities and strategies a country could employ within these domains.
#
# Request Format:
#
# Please provide a comprehensive overview of possible military actions in a specified domain for a given country. The response should include both offensive and defensive strategies, highlighting the domain's unique aspects and the hypothetical capabilities of the country in that domain.
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
#         "overview": "A brief comment on the country's military capabilities and strategic posture within this domain.",
#         "offensive_actions": [
#             {
#                 "action": "Name of the offensive action",
#                 "combat_strength": "Estimated combat strength or force size involved in the action in terms of personnel, equipment, or other relevant metrics",
#                 "description": "A detailed description of the action, including its strategic purpose and expected impact",
#                 "range": "Provide the operational range of the action in kilometers (e.g., 5, 10, 50, 100 km) where applicable. For actions in domains where a physical range is not relevant (e.g., certain cyberspace operations), specify as "Not Applicable" instead of "0" to indicate the nature of the action does not involve a measurable physical distance.
#             },
#             ... // (4 more actions)
#         ],
#         "defensive_actions": [
#             {
#                 "action": "Name of the defensive action",
#                 "combat_strength": "Estimated combat strength or force size involved in the action in terms of personnel, equipment, or other relevant metrics",
#                 "description": "A detailed description of the action, focusing on its defensive objectives and implementation",
#                 "range": "Provide the operational range of the action in kilometers (e.g., 5, 10, 50, 100 km) where applicable. For actions in domains where a physical range is not relevant (e.g., certain cyberspace operations), specify as "Not Applicable" instead of "0" to indicate the nature of the action does not involve a measurable physical distance.
#             },
#             ... // (4 more actions)
#         ]
#     }
# ]
#
# Guidelines for Action Descriptions:
#
#     Offensive Actions: List and describe 5 hypothetical offensive actions the country could take within the specified domain. Include details on the nature of each action, the forces involved, their combat strength, and the action's range and strategic objectives.
#
#     Defensive Actions: List and describe 5 hypothetical defensive actions the country could implement within the specified domain. Detail the defensive strategy, the size and strength of forces allocated, the nature of defensive measures, and their effective operational range.
#
# This structured approach will provide a clear and detailed view of potential military actions within a specific domain, aiding in the comprehensive analysis of MDO capabilities and strategies.
# """
#
#
# def generate_actions(country, domain):
#     print(f"Getting {country} {domain} domain actions")
#     docs = ExternalDatabase.get(country, domain)
#     print(f"Got {len(docs)} docs")
#     modified_system_prompt = system_prompt
#     if docs:
#         raw_text = "\n\n".join(docs)
#         modified_system_prompt = system_prompt % f"""This is additional information about {country} and {domain} domain:\n\n{raw_text}"""
#     response = GPT.get_response(
#         [
#             {"role": "system", "content": modified_system_prompt},
#             {"role": "system", "content": f"Provide a list of {domain} domain actions for the {country} country"}
#         ], "gpt-35-16k", 2000
#     )
#     return response
#
#
# if __name__ == '__main__':
#     domain = "cyberspace"
#     country = "Lithuania"
#     response = generate_actions(country, domain)
#     pprint(response)
#     with open(f"{domain}_{country}.json", "w") as f:
#         json.dump(response, f, indent=4, ensure_ascii=False)
#
# # for domain in ["land", "maritime", "air", "space", "cyberspace"]:
# #     for country in ["Russia", "Lithuania"]:
# #         response = GPT.get_response(
# #             [
# #                 {"role": "system", "content": system_prompt},
# #                 {"role": "system", "content": f"Provide a list of {domain} domain actions for the {country} country"}
# #             ]
# #         )
# #         print(response)
# #         with open(f"{domain}_{country}.json", "w") as f:
# #             json.dump(response, f, indent=4, ensure_ascii=False)
#
# # domain = "land"
# # country = "Lithuania"
# # response = GPT.get_response(
# #             [
# #                 {"role": "system", "content": system_prompt},
# #                 {"role": "system", "content": f"Provide a list of {domain} domain actions for the {country} country"}
# #             ]
# #         )
# # pprint(response)
