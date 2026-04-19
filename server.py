from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, render_template, request 

app = Flask("Emotion detector")

@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    detector_response = emotion_detector(text_to_analyze=text_to_analyze)
    
    if detector_response['dominant_emotion'] == None:
        return "Invalid text! Please try again!"

    return (f"For the given statement, the system response is "
            f"\'anger\': {detector_response['anger']}, "
            f"\'disgust\': {detector_response['disgust']}, "
            f"\'fear\': {detector_response['fear']}, "
            f"\'joy\': {detector_response['joy']} and "
            f"\'sadness\': {detector_response['sadness']}. "
            f"The dominant emotion is <b> {detector_response['dominant_emotion']}. </b>"
            )
