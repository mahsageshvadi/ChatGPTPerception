import sys
sys.path.append('../EXP/')
import requests

class Query:
    @staticmethod
    def query(question, data):
        # OpenAI API Key
        api_key = "********************************"
        # Getting the base64 string
        base64_image = data

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": question
                },
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{base64_image}"
                }
                }
            ]
            }
        ],
        "max_tokens": 300
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

        content_string = response.json()['choices'][0]['message']['content']
        return content_string  
