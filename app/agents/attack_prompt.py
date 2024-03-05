import asyncio

from agents.gpt import GPTChainer
from gameplay.game_state import GameState
from resources import Dictionary


async def analyze_outcome_status(attack_scenario):
    system_prompt = f"""
    You are tasked with simulating a military engagement between two nations using advanced war simulation AI. Your objective is to calculate the outcome of the action that user selected and according to that disable or enable the units that attacking or defending team has. To achieve this, you must consider a comprehensive range of factors that influence military conflict outcomes.
    
    Please keep in mind the following aspects:
    
        Attacking Country Profile:
            Military Capabilities: Detail the size, technological level, and composition of the attacking nation's armed forces, including land, air, sea, cyber, and space assets.
            Economic Resilience: Describe the economic stability and war-sustaining capabilities of the attacker, including GDP, resource access, and industrial base.
            Strategic Intentions: Outline the strategic objectives, including territorial, political, or economic goals.
    
        Defending Country Profile:
            Military Strength: Provide information on the defender's military forces, emphasizing defensive capabilities, fortifications, and home advantage.
            Geographical Factors: Consider natural barriers, climate, and the logistical challenges posed by the defending country's terrain.
            Economic and Civilian Resilience: Assess the economic stability and civilian morale, highlighting any factors that might impact the defender's long-term resistance capabilities.
    
        Historical and Political Context:
            Historical Conflicts: Analyze previous engagements between the two nations, focusing on outcomes, lessons learned, and unresolved tensions.
            Current Political Climate: Evaluate the internal and international political situation, including alliances, treaties, and global opinion.
    
        Additional Considerations:
            International Alliances and Support: Detail the potential involvement of international allies or organizations and their likely impact on the conflict.
            Cyber and Space Warfare Capabilities: Account for non-traditional warfare avenues, including cyber attacks on infrastructure and the use of satellites for intelligence and communication.
            Rules of Engagement: Consider any legal or ethical constraints on military operations, such as international laws and avoidance of civilian casualties.
    
    There are the types in the war simulation:
    {Dictionary.get_json_types()}
    
    These are the unit types with the descriptions:
    {Dictionary.get_json_units()}
    
    Upon receiving this input, simulate the outcomes of the given attack, taking into account the dynamic nature of warfare where unforeseen events can significantly alter the course of the conflict. Return a JSON object containing:
    
        Title: A short name for the attack and it's possible outcomes.
        Status: Return success if the attack was successful and return fail if the attack failed.
        Description: A description of the attack and its outcome. If some of the units were destroyed or deployed, describe those as well.
        Affected objects: A list of objects that were affected by the action. Add only the objects that each player had in the initial game state and only those, whose status was changed during this turn.
    
    This structured approach ensures a thorough analysis, enhancing the realism and depth of the simulation.
    """

    # attack_scenario = {
    #     "team": "red",
    #     "attacker_units": {
    #         "domain": "land",
    #         "unit": "artillery",
    #         "location": "Minsk"
    #     },
    #     "target_units": {
    #         "domain": "land",
    #         "unit": "power plant",
    #         "location": "Visaginas"
    #     },
    #     "title": "Precision Artillery Strike",
    #     "description": "Use advanced targeting systems to perform a precision strike on the enemy's artillery units in Vilnius, minimizing collateral damage.",
    #     "probability": 0.7,
    #     "escalation": 0.9,
    # }

    attack_prompt = f'''
    Attacking team: red team
    Defending country: blue team
    Turn: Red team
    
    Generate the consequences of the attack done by the attacking team on both - the attacking team and the defending team resources.
    The parameters of the attack are given in the JSON file:
    {attack_scenario}
    
    To see if the attack is valid, please check the given game state (the units section), where all the units of both teams are given. If the team has selected units, the attack is valid. If the team does not have the selected units, the attack is considered as failed.
    The current game state is described here:
    {GameState.get_state()}
    
    According to the given attack probability and the given attack and both players context, evaluate if the attack was successfull. Regarding the success of the attack, evaluate the consequences of the attack.
    Also calculate the global conflict status before and after the attack.
    The consequences of the attack should be given in json format like this:
    
    Return a JSON and only in JSON, use this template. Refer to the given game state and units of both teams when evaluating the consequences of the event.
    
    JSON response:
    {{
        "title": "the title of the attack (up to 8 words)",
        "description": "the description of the consequences. If there were units destroyed or deployed, or if there were any other changes, describe them in this field as well (up to 3 sentences)",
        "status": "1 if the attack was successfull and 0 if it failed (bool, 0 or 1)",
        "global_conflict" : "value of the global conflict status (float),
        "affected_units": {{
            "blue": [
                {{
                    "name": "name of the unit",
                    "condition": "based on the attack, the condition of the unit (working, failed, destroyed, disabled, captured, etc.)",
                    "location": "the county where this resource is placed (null if it does not have a physical location)"
                }},
            ...
            ]
            "red": [
                {{
                    "name": "name of the unit",
                    "condition": "based on the attack, the condition of the unit (working, failed, destroyed, disabled, captured, etc.)",
                    "location": "the county where this resource is placed (null if it does not have a physical location)"
                }},
            ...
            ]
        }},
        "affected_domains": [
            {{
                "name": "name of the domain",
                "comment": "a comment about effects on the domain (up to 3 sentences)
            }}
        ]
    }}
    '''

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": attack_prompt},
    ]

    response = await GPTChainer().add_messages(messages).send_async()
    print(f"response: {response}")
    return response



if __name__ == '__main__':
    attack_scenario = {'title': 'Attack Ministry of Economics with drone',
                  'description': 'Send a drone to attack the Ministry of Economics in the cyberspace domain.',
                  'outcome': "If successful, the attack can disrupt the defender's economic management and potentially weaken their overall war effort.",
                  'probability': 0.7, 'escalation': 0.1}
    print(asyncio.run(analyze_outcome_status(attack_scenario)))