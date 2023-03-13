### TO RUN ###
# Input the below into the terminal
# python3 generate-script.py "[what you want the script to do]" "[programming language]" "[output file name]"

import requests
import argparse
import os

# Parameterise script to pass prompt as input: python3 generate-script.py "insert python task here"
parser = argparse.ArgumentParser()
parser.add_argument('prompt', help='The prompt to send to the OpenAI API')
parser.add_argument('language', help='The programming language you would like the script written in')
parser.add_argument('file_name', help='Name of file to save python script as')
args = parser.parse_args()

# API connection
api_endpoint = 'https://api.openai.com/v1/completions'
api_key = os.getenv('OPENAI_API_KEY') # run in terminal: export OPENAI_API_KEY=[insert api key here]
request_headers = {
    'Content-Type' : 'application/json',
    'Authorization': 'Bearer ' + api_key
}
request_data = {
    'model': 'text-davinci-003',
    'prompt': f'Write a script to {args.prompt} in {args.language}. Provide only code, no text.',
    'max_tokens': 100, # control length of response. Sets limit of words / punctuation
    'temperature': 0.5 # level of creativity (1 = max creativity, 0 = precise and predictable)
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

# Run request - writes output to new py file
if response.status_code == 200:
    response_text = response.json()['choices'][0]['text']
    with open(args.file_name, 'w') as file:
        file.write(response_text)
else:
    print(f'Request failed with status code: {str(response.status_code)}')