import requests
import json
from typing import Union

def make_tts_api_request(sourceLanguage: str, tts_service_id: str, asr_output: str, url: str) -> Union[dict,None]:
    """
    Make test-to-speech api request
    """
    headers = {
        "Authorization" : "1M569xUGsgDNmFmb9SIx_mmGMtv-b8AnHt1AOB_U8fUS9_2wYenbGtosytBjDzHM",
        "Content-Type": "application/json",
    }

    payload= {"pipelineTasks": [       
        {
            "taskType": "tts",
            "config": {
                "language": {
                    "sourceLanguage": sourceLanguage
                },
                "serviceId": tts_service_id,
                "gender": "female"
            }
        }
    ],
    "inputData": {
        "input": [
            {
                "source": asr_output
            }
        ]
    }
    }

    payload_json= json.dumps(payload)

    response = requests.post(url, headers=headers, data=payload_json)
    if response.status_code ==200:
        response=response.json()
        return response
    else:
        print("Request failed with status code:", response.status_code)
        return None
    

def make_translation_request(target_language: str, translation_service_id: str, input_text: str, url: str) -> Union[dict,None]:
    """
    Make translation api request 
    """
    headers =  {
        "Authorization" : "1M569xUGsgDNmFmb9SIx_mmGMtv-b8AnHt1AOB_U8fUS9_2wYenbGtosytBjDzHM",
        "Content-Type": "application/json",
    }  

    payload = {
    "pipelineTasks": [
        {
            "taskType": "translation",
            "config": {
                "language": {
                    "sourceLanguage": "en",
                    "targetLanguage": target_language
                },
                "serviceId": translation_service_id
            }
        }
    ],
    "inputData": {
        "input": [
            {
                "source": input_text
            }
        ]
    }
}

    payload_json= json.dumps(payload)

    response = requests.post(url, headers=headers, data=payload_json)
    if response.status_code ==200:
        response=response.json()
        return response
    else:
        print("Request failed with status code:", response.status_code)
        return None