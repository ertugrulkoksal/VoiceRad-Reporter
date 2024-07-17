from flask import Flask, request, jsonify
from openai import OpenAI
import os

api_key = "OPENAI API KEY"
client = OpenAI(api_key=api_key)
#First Upload File and Then Open

app = Flask(__name__)

@app.route('/api/convert-audio', methods=['POST'])
def convert_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file = request.files['audio']
    audio_file.save(os.path.join(r"C:\Users\ertug\Desktop\Python\STT", audio_file.filename)) #Yükleme Adresi
    print(audio_file.filename)
    print(type(audio_file))

    try:
        transcribe_response = client.audio.transcriptions.create(
            model="whisper-1",
            file=open(audio_file.filename, 'rb'),
            language='tr'
        )
        # os.remove(r"C:\Users\ertug\Desktop\Python\STT\audio_file.filename")
        print(type(audio_file))
        transcription_text = transcribe_response.text
        print("OpenAI'dan dönen metin:", transcription_text)

        return jsonify({'text': transcription_text}), 200
    except Exception as e:
        print('Hata:', e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
