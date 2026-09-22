# Generate a Blog with OpenAI 📝

import openai
import os
from dotenv import dotenv_values
from openai import OpenAI

config = dotenv_values('.env')
api_key = config.get('OPENAI_API_KEY') or os.getenv('OPENAI_API_KEY')

def generate_blog(paragraph_topic):
  if not api_key:
    raise RuntimeError('Set OPENAI_API_KEY in .env or the environment before running this script.')

  client = OpenAI(api_key=api_key)
  response = client.completions.create(
    model = 'gpt-3.5-turbo-instruct',
    prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
    max_tokens = 400,
    temperature = 0.3
  )
  retrieve_blog = response.choices[0].text
  return retrieve_blog

keep_writing = True

while keep_writing:
  answer = input('Write a paragraph? Y for yes, anything else for no. ')
  if (answer == 'Y'):
    paragraph_topic = input('What should this paragraph talk about? ')
    try:
      print(generate_blog(paragraph_topic))
    except Exception as error:
      print(f'Unable to generate the blog: {error}')
  else:
    keep_writing = False