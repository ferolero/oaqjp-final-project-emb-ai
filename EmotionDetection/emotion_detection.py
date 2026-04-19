import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } } 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    nlp_response = requests.post(url, json = myobj, headers = header)

    if nlp_response.status_code == 200:
        formatted_response = json.loads(nlp_response.text)
        scores = {
                "anger":formatted_response["emotionPredictions"][0]["emotion"]["anger"], 
                "disgust":formatted_response["emotionPredictions"][0]["emotion"]["disgust"],
                "fear":formatted_response["emotionPredictions"][0]["emotion"]["fear"],
                "joy":formatted_response["emotionPredictions"][0]["emotion"]["joy"],
                "sadness":formatted_response["emotionPredictions"][0]["emotion"]["sadness"]
                }
        dominant_emotion = max(scores, key=scores.get)
        scores["dominant_emotion"] = dominant_emotion
        return scores
    elif nlp_response.status_code == 400:
        return {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}
    else:
        return {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}
