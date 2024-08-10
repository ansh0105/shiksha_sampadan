import base64
from datetime import datetime

def base64_to_wav(base64_data: str) -> str:
    """
    Decode base64 data and write it down and generate .wav audio file  
    """
    binary_data = base64.b64decode(base64_data)
    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    file_path = "audio_dir\\"+date_string+"output.wav"

    with open(file_path, "wb") as wav_file:
        wav_file.write(binary_data)

    return file_path