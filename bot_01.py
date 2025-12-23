from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# def fix_grammar(text):
#   llm = OpenAI()
#   response = llm.responses.create(
#     model="gpt-4.1-mini",
#     temperature=1,
#     input=f"Print out the input text with the grammar fixed: {text}"
#   )

#   return response.output_text

# user_input = input("Tell me a sentence and I'll fix the grammar: \n")

# print(fix_grammar(user_input))

# def words_to_number(text):
#   llm = OpenAI()
#   response = llm.responses.create(
#     model="gpt-4.1-mini",
#     temperature=1,
#     input = f"take the number written in text and print the actual numbers with as few words as possible {text} "
#   )
#   return response.output_text

# user_input = input("Write out a number in words, and I'll turn it into numbers: \n")

# print(words_to_number(user_input))


# def opposite(text):
#   llm = OpenAI()
#   response = llm.responses.create(
#     model = "gpt-4.1-mini",
#     temperature = 1,
#     input = f"take the following  text and write the opposite with no other text: {text}"
#   )
#   return response.output_text

# user_input = input("Write a word and I'll say the opposite:\n")
# print(opposite(user_input))

# def feelings(text):
#   llm = OpenAI()
#   response = llm.responses.create(
#     model = "gpt-4.1-mini",
#     temperature = 1,
#     input = f"take the following text and give a one word emotion that describes it with no other text: {text}"
#   )
#   return response.output_text

# user_input = input("write a sentence and I'll tell you what the feeling behind it is: \n")
# print(feelings(user_input))

