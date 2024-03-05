import asyncio
import json
import os

import openai
from dotenv import load_dotenv
from openai.lib.azure import AsyncAzureOpenAI

load_dotenv()

API_KEY = os.environ.get("KEY")


def _parse_to_json(response):
    try:
        return json.loads(response)
    except Exception as e:
        return str(response)


class GPTChainer:
    def __init__(self):
        self.messages = []

    def add_messages(self, messages):
        self.messages.extend(messages)
        return self

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})
        return self

    async def send_async(self, model="gpt-4-uncensored", max_tokens=1024, parse_json=True):
        client = AsyncAzureOpenAI(
            # This is the default and can be omitted
            api_key=API_KEY,
            api_version="2023-07-01-preview",
            azure_endpoint="https://openai-tide-hackathon.openai.azure.com/",
        )
        result = await client.chat.completions.create(messages=self.messages, model=model, max_tokens=max_tokens)
        if parse_json:
            return _parse_to_json(result.choices[0].message.content)
        return result.choices[0].message.content

    def send(self, model="gpt-4-uncensored", max_tokens=1024, parse_json=True):
        client = openai.AzureOpenAI(
            api_key=API_KEY,
            api_version="2023-07-01-preview",
            azure_endpoint="https://openai-tide-hackathon.openai.azure.com/",
        )
        result = client.chat.completions.create(messages=self.messages, model=model, max_tokens=max_tokens)
        if parse_json:
            return _parse_to_json(result.choices[0].message.content)
        return result.choices[0].message.content


class GPT:

    @classmethod
    def get_response(cls, messages, model="gpt-4-uncensored", max_tokens=1024):
        client = openai.AzureOpenAI(
            # This is the default and can be omitted
            api_key=API_KEY,
            api_version="2023-07-01-preview",
            azure_endpoint="https://openai-tide-hackathon.openai.azure.com/",
        )

        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model,
            max_tokens=max_tokens,
        )

        try:
            message = chat_completion.choices[0].message.content
            return cls._parse_to_json(message)
        except Exception as e:
            return str(e)

    @classmethod
    def fix_json(cls, bad_json):
        response = cls.get_response([
            {"role": "system", "content": "Fix the JSON. Return only a valid JSON object."},
            {"role": "user", "content": str(bad_json)}]
        )
        return response


if __name__ == '__main__':
    # messages = [
    #     {"role": "system", "content": "You are an AI assistant that helps people find information."}
    # ]
    # print(GPT.get_response(messages))
    # # response = asyncio.run(GPT.get_response(messages))
    # print(response)
    msg = GPTChainer()
    coroutine = msg.add_message("system", "You are an AI assistant that helps people find information.").add_message(
        "user", "What is the capital of France?").send_async()
    print(asyncio.run(coroutine))
