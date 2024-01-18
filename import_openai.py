import openai
from apikey import APIKEY

openai.api_key = APIKEY

output = openai.ChatCompleation(
    model="gpt-3.5-turbo",
    message=[{"role":"user", "content": "Write me a script of python integrated with openai"}]
)

print(output)