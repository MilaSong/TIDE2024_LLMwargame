# import json
# from pprint import pprint
#
# from app.gameplay.game_state import GameState
# from app.resources import Dictionary
# from app.resources.knowlage import ExternalDatabase
# from app.agents.gpt import GPT
#
#
# def get_actions(attacker, target):
#     system_prompt = f"""
#     As a data analyst conducting research on Multi-Domain Operations (MDO), I am exploring the
#     strategic and tactical actions within various domains of military operations, including maritime, land, air, space,
#     and cyberspace. My objective is to analyze the potential offensive and defensive capabilities and strategies a
#     country could employ within these domains.
#
#     There are the types in the war simulation:
#     {Dictionary.get_json_types()}
#
#     These are the unit types with the descriptions:
#     {Dictionary.get_json_units()}
#
#     Please provide a comprehensive overview of possible military actions in a specified domain for a given country. The
#     response should include both offensive and defensive strategies, highlighting the domain's unique aspects and the
#     hypothetical capabilities of the country in that domain.
#
#     %s
#
#     Response Structure:
#
#     json
#
#     [
#         {{
#             'title': 'a brief title of the action',
#             'description': 'a detailed description of a suggested action',
#             'outcome': 'the expected outcome of the action',
#             'escalation': "a float from 0-1 based on the escalation to the global conflict",
#             'probability': "a float from 0-1 based on the probability of the action succeeding",
#         }} .. 4 more
#     ]
#     """
#
#
#     user_prompt = f"""
#     Provide a list of actions
#
#     response = GPT.get_response(
#         [
#             {"role": "system", "content": system_prompt},
#             {"role": "system", "content": f"Provide a list of {domain} domain actions for the {country} country"}
#         ], "-16k", 2000
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
