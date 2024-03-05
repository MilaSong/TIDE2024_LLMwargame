from pprint import pprint

from agents.gpt import GPT

#
# system_prompt = """
# You are a war simulator AI.
# I will provide an attack vector from one country to another.
# I will also provide the defense vector of the country being attacked.
#
# Calculate the probability of a successful attack.
# Take in mind a size of the attacking country, size of the defending country.
# A history of the two countries, and the current political climate.
#
# Return a JSON object with the probability of a successful attack and a brief explanation as to why, and a comment about fictional outcome of the attack.
#
# {
#     "probability": (float),
#     "explanation": (string),
#     "comment": (string),
#     "outcome": (string)
# }
#
# """

system_prompt = """
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

Upon receiving this input, simulate the conflict scenario, taking into account the dynamic nature of warfare where unforeseen events can significantly alter the course of the conflict. Return a JSON object containing:

    Probability: A float value representing the likelihood of a successful attack.
    Explanation: A brief narrative explaining the key factors influencing the outcome.
    Comment: Insights on notable aspects or turning points in the simulated scenario.
    Outcome: A fictional account of the aftermath and broader implications of the conflict.

This structured approach ensures a thorough analysis, enhancing the realism and depth of the simulation.
"""

attack_vector = """
Attacking country: Lithuania
Defending country: Russia

Attack vector:
{
     "action": "Airstrikes",
     "comment": "Lithuania can launch precision airstrikes on enemy targets, including infrastructure, military installations, and enemy forces."
}

Defense vector:
{
    "action": "Air defense operations",
    "comment": "Russia has a robust air defense system consisting of surface-to-air missiles, anti-aircraft artillery, and advanced radar systems to protect its airspace."
},
{
    "action": "Combat air patrol",
    "comment": "Russia maintains a continuous presence of fighter jets on combat air patrol to detect and intercept any hostile aircraft entering its airspace."
},
{
    "action": "Anti-aircraft warfare",
    "comment": "Russia has a wide range of anti-aircraft systems, including surface-to-air missiles and anti-aircraft artillery, to defend against enemy air attacks."
},
{
    "action": "Electronic warfare",
    "comment": "Russia possesses advanced electronic warfare capabilities to disrupt and disable enemy aircraft and their communication systems."
},
{
    "action": "Airfield defense",
    "comment": "Russia has measures in place to defend its airfields from enemy attacks, including perimeter security, anti-aircraft systems, and quick reaction forces."
}

Return a JSON object with the probability of a successful attack and a brief explanation as to why, and a comment about fictional outcome of the attack.
"""
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": attack_vector},
]

response = GPT.get_response(messages)

pprint(response)
