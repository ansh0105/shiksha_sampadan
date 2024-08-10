import time
from bhashini_utils.config import *
from bhashini_utils.postman_api import *
from bhashini_utils.extra_helper import base64_to_wav
from typing import Tuple

def speak(source_language: str,answer: str) -> Tuple[str,str]:
    """
    Function helps to integrate translation and text to speech service from Bhashini 
    """
    url= API_ENDPOINT
    if source_language =="en":
        translation_service_id = None
        tts_service_id= TTS_SERVICE_ID_EN
        
    elif source_language == "hi":
        translation_service_id = TRANSLATION_SERVICE_ID_EN_HI
        tts_service_id= TTS_SERVICE_ID_HI

    elif source_language == "kn":
        translation_service_id = TRANSLATION_SERVICE_ID_EN_KN
        tts_service_id= TTS_SERVICE_ID_TE

    elif source_language =="bn":
        translation_service_id =TRANSLATION_SERVICE_ID_EN_BN
        tts_service_id=TTS_SERVICE_ID_BN
    

    if source_language == 'en':
        tts_result=make_tts_api_request(source_language,tts_service_id,answer,url)
        audio_file_path = base64_to_wav(tts_result["pipelineResponse"][0]["audio"][0]["audioContent"])
        time.sleep(0.5)
        return audio_file_path, answer
    else:
        translation_result = make_translation_request(source_language,translation_service_id,answer,url)
        tts_result =make_tts_api_request(source_language,tts_service_id,translation_result["pipelineResponse"][0]["output"][0]["target"],url)
        audio_file_path = base64_to_wav(tts_result["pipelineResponse"][0]["audio"][0]["audioContent"])
        time.sleep(0.5)
        return audio_file_path, translation_result["pipelineResponse"][0]["output"][0]["target"]




