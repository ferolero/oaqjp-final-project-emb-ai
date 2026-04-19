''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the score per emotion
        and specifies the dominant_emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    detector_response = emotion_detector(text_to_analyze=text_to_analyze)

    if detector_response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (f"For the given statement, the system response is "
            f"\'anger\': {detector_response['anger']}, "
            f"\'disgust\': {detector_response['disgust']}, "
            f"\'fear\': {detector_response['fear']}, "
            f"\'joy\': {detector_response['joy']} and "
            f"\'sadness\': {detector_response['sadness']}. "
            f"The dominant emotion is <b> {detector_response['dominant_emotion']}. </b>"
            )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
