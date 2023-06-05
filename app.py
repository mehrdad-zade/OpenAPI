from flask import Flask, request, jsonify, render_template
from openAI.gpt import chatGPT3_response, chatGPT4_response

app = Flask(__name__)

@app.route('/api/question', methods=['POST'])
def get_answer():
    question = request.json.get('question') # get the question from html q-box using /api/receive_question POST
    answer = chatGPT3_response(question)
    return jsonify({'answer': answer})

# Route to receive the question text
@app.route('/api/receive_question', methods=['POST'])
def receive_question():
    question = request.json.get('question')
    return jsonify({'message': 'Question received'})

@app.route('/api/question')
def index():
    return render_template('index.html')


# run instructions:
# FLASK_APP=app.py flask run  
