import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"

#structure it
from pydantic import BaseModel

class Ticket(BaseModel):
    name: str
    email: str
    issue: str

schema=Ticket.model_json_schema()

response_format={
    "type": "json_object"
}

system_prompt=f"""
Extract the personal information from the customer ticket strictly based on this schema and give a json output: {schema}"""

text="Hello My name is Satyam Jha.I have purchased a new smartphone from your shop which stops working.My address is Kolkata.My Phone number is 9675845423.My email id is satyamjha@example.com."
prompt=f"""
This is a Customer Ticket. Please extract the personal information from this.
{text}
"""

message_system={
    "role": "system",
    "content": system_prompt
}

message={
    "role": role,
    "content": prompt
}

messages=[message_system, message]

response=client.chat.completions.create(model=model, messages=messages, response_format=response_format)

answer=response.choices[0].message.content
print(answer)

import json
raw_json=answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)

