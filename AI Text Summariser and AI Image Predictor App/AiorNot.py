import requests
import json
import os

def labels(filename):

    payload = json.dumps({
      "inputs": filename
    })

    headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {os.getenv("ACCESS_TOKEN")}'
        }

    response = requests.post('https://api-inference.huggingface.co/models/Nahrawy/AIorNot',
                                  headers=headers,
                                  data=payload)

    return response.text
