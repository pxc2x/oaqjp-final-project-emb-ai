import requests
import json 

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, headers=headers, json=input_json)
    response_dict = json.loads(response.text)
    emotion_dict = response_dict["emotionPredictions"][0]["emotion"]
    dominant_emotion = ""
    dominant_emotion_score = 0
    for key, val in emotion_dict.items():
        if val > dominant_emotion_score:
            dominant_emotion = key
            dominant_emotion_score = val
    emotion_dict["dominant_emotion"]= dominant_emotion
    return emotion_dict
