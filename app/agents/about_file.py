from agents.gpt import GPTChainer

system_prompt = f"""
    You are military data analyst who's been asked to evaluate and analyze a provided text.
    The text is can be any text.
    Extract the following information from the text:
    You are expected to provide a JSON response with the following fields:
    
    Extract paragraphs from the text and provide a summary of the text.
    JSON response:
    {{
        "domains": "the list domains that this information is relevant to ", " comma separated (land, air, maritime, space, cyberspace)",
        "country": "the coutry for which this paragraph is relevant",
        "category": "the category of the paragraph (e.g. military, political, economic, etc.)",
        "paragraph": "the paragraph text of the article. Include as much information as possible that is relevant to the category",
        "summary": "a summary of the paragraph"
    }}
    """


async def analyze_text(text):
    """
    This function is used to analyze a given text and extract the following information from the text:
    :param text:
    :return:
    """
    return await GPTChainer().add_message("system", system_prompt).add_message("user", text).send_async()
