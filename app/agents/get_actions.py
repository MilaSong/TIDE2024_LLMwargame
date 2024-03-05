from pprint import pprint
import json

from agents.gpt import GPT, GPTChainer
from gameplay.game_state import GameState
from resources import Dictionary


async def get_actions(attacker, target, range):
    system_prompt = f"""
    You are tasked with simulating a military engagement between two nations using advanced war simulation AI. Your objective is to calculate the likelihood of a successful attack by one country (the attacker) on another (the defender). To achieve this, you must consider a comprehensive range of factors that influence military conflict outcomes.
    
    Please provide detailed inputs for the following aspects:
    
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
        
    Upon receiving this input, simulate the conflict scenario, taking into account the dynamic nature of warfare where unforeseen events can significantly alter the course of the conflict. Return a JSON object containing:
    
        Probability: A float value representing the likelihood of a successful attack.
        Explanation: A brief narrative explaining the key factors influencing the outcome.
        Comment: Insights on notable aspects or turning points in the simulated scenario.
        Outcome: A fictional account of the aftermath and broader implications of the conflict.
    
    This structured approach ensures a thorough analysis, enhancing the realism and depth of the simulation.
    """

    event = {
        "id": 1,
        "team": "red",
        "attacker_units": {
            "domain": "land",
            "unit": "artillery",
            "location": "Minsk"
        },
        "target_units": {
            "domain": "land",
            "unit": "power plant",
            "location": "Visaginas"
        }
    }

    attack_vector = f'''
    Attacking team: Red team (Russia, Belarus)
    Defending country: NATO countries (Baltic states with the help of Sweden and Ukraine)
    Turn: Red team
    
    Generate 5 possible actions for the team that's doing their turn. The actions should be done only using the attacker and the target units. They should act in the given attacker and defender domain.
    The attacker selected the units described in the given JSON file:
    
    The team that is making an action using the selected attacker and target units which are described by the given json files:
    
    Attacker: 
    {attacker}
    Target: 
    {target}
    Range between the attacker and the target: {range}
    
    Please, do not generate any moves that do not use thse units or do not operate in the given domain.
    
    Also, keep in mind the current game state, which is:
    {GameState.get_state()}
    
    Given the information about the Blue and Red teams and the current game state, generate 5 possible scenarious of what could the attacking team do with the given objects.
    Return the 5 possible actions using JSON format.
    Keep in mind that the actions should be done in the given attacker and target domain, and not other domains. 
    The actions should be done in the given attacker and target domain, and not other domains. It should have this structure:
    
    {{"results": [
        {{
            "title": "A short title of the possible action (up to 6 words)",
            "description": "A detailed description of the move (up to 2 sentences)",
            "outcome": "A description of possible outcome if this action would be chosen (given the current game state)",
            "probability": "The likelihood of a successful event (float, from 0 to 1)",
            "escalation": "Escalation of global conflict. The global conflict involves many of the biggest countries of the world, (float, from 0 meaning low escalation to 1 meaning total world war)"
        }},
        {{
            ... 4 more
        }},
        ...
    ]}}
    
    This list must have 5 entries JSON in it, each representing different move that you suggest. Return only the list of JSONs as an output and nothing else.
    '''

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": attack_vector},
    ]
    response = await GPTChainer().add_messages(messages).send_async()
    print(f"response: {response}")
    return response


if __name__ == '__main__':
    attacker = {
        "domain": "land",
        "unit": "artillery",
        "location": "Minsk"
    }
    target = {
        "domain": "land",
        "unit": "power plant",
        "location": "Visaginas"
    }
    get_actions(attacker, target, "20km")
