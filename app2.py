from flask import Flask, request, jsonify
import speech_recognition as sr

app = Flask(__name__)

@app.route('/api/convert-audio', methods=['POST']) 

def convert_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file = request.files['audio']
    print(audio_file)

    r = sr.Recognizer()

    try:

        with sr.AudioFile(audio_file) as source:
            audio_data = r.record(source)

            text = r.recognize_google(audio_data, language="tr")
            print(text)
            return jsonify({'text': text}), 200

    except Exception as e:
        print('Hata:', e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
