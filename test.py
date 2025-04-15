import litellm
import os
litellm._turn_on_debug()
response = litellm.completion(
    model="anthropic/gcp-claude37-sonnet",               # add `openai/` prefix to model so litellm knows to route to OpenAI
    api_key="54nhP5uBXv7iWgHJ4bWMD90Nwkn09BXN",                  # api key to your openai compatible endpoint
    api_base="https://gpt-i18n.byteintl.net/gpt/openapi/online/v2/crawl",     # set API Base of your Custom OpenAI Endpoint
    messages=[
                {
                    "role": "user",
                    "content": "北京天气怎么样",
                }
    ],
    system= "you are a very helpful assistant",
    tools= [
        {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA"
                        }
                    }
                }
            }
        }
    ],
    tool_choices= {
        "type": "function",
        "function": {
            "name": "my_function"
        }
    }
)
print(response)
