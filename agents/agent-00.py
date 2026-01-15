import yagmail
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def send_email(body):
  yag = yagmail.SMTP(os.getenv("GMAIL_ACCOUNT"), os.getenv("GMAIL_APP_PASSWORD"))
  yag.send(to="mbcheruff@gmail.com", subject="Test Email", contents=body) 


send_email("hey there")