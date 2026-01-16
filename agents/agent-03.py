import yagmail
import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()
llm = OpenAI()

TOOLS = [
  {
    "type": "function",
      "name": "send_email",
      "description": "Send an email containing a specific subject and body to a specific recipient.",
      "parameters": {
          "type": "object",
          "properties": {
            "recipient_email": { "type": "string" },
            "subject": { "type": "string" },
            "body": { "type": "string" },
          },
          "required": ["recipient_email", "subject", "body"]
      },
  }
]

def send_email(recipient_email, subject, body):
  yag = yagmail.SMTP(os.getenv("GMAIL_ACCOUNT"), os.getenv("GMAIL_APP_PASSWORD"))
  yag.send(to=recipient_email, subject=subject, contents=body) 

def system_prompt():
  return f"""You are a friendly AI assistant who helps human users. In addition to your ability to converse with the user, you are equipped with the ability to send an email if the user so desires.

    Here's how to send an email. You first need to ensure that you have three pieces of information:

    1) The recipient email address
    2) The email subject
    3) The email body

    Then, when you're ready to send the email, use the send_email tool. """

assistant_message = "How can I help?"
user_input = input(f"\nAssistant: {assistant_message}\n\nUser: ")

history = [
  {"role": "developer", "content": system_prompt()},
  {"role": "assistant", "content": assistant_message},
  {"role": "user", "content": user_input}
]

while user_input != "exit":
  response = llm.responses.create(
    model="gpt-4.1-mini",
    temperature=1.0,
    input=history,
    tools = TOOLS
  )
  llm_response_text = f"\nAssistant: {response.output_text}"

  for item in response.output:
    if item.type == "function_call":
      print(item)
      function_call = item
      function_name = item.name
      args = json.loads(item.arguments)

      if function_name == "send_email":
        results = {"send_email": send_email(**args)}

        llm_response_text = "\nAssistant: I've sent your email! What else can I do to help?"

  print(llm_response_text)

  user_input = input("\nUser: ")
  history += [
    {"role": "assistant", "content": response.output_text},
    {"role": "user", "content": user_input}
  ]

